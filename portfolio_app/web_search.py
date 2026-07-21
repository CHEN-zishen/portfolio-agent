import html
import re
from dataclasses import dataclass
from html.parser import HTMLParser
from typing import Dict, List
from urllib.parse import parse_qs, quote_plus, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from .config import WEB_SEARCH_MAX_PAGES, WEB_SEARCH_MAX_RESULTS, WEB_SEARCH_TIMEOUT


APPLICATION_TERMS = [
    "申请", "录取", "留学", "学校", "院校", "大学", "项目", "专业", "硕士", "博士",
    "研究生", "导师", "教授", "课程", "官网", "要求", "截止", "文书", "套磁",
    "优势", "匹配", "适合", "application", "admission", "admissions", "apply",
    "university", "college", "school", "program", "programme", "master", "msc",
    "phd", "requirements", "deadline", "curriculum", "faculty", "professor",
    "supervisor", "statement of purpose", "sop", "personal statement", "fit",
    "advantage", "strength", "scholarship",
]

SCHOOL_HINTS = [
    "cmu", "mit", "stanford", "berkeley", "ucsd", "ucla", "usc", "cornell",
    "columbia", "upenn", "harvard", "oxford", "cambridge", "imperial", "ucl",
    "nus", "ntu", "hku", "hkust", "cuhk", "polyu", "cityu", "toronto",
    "waterloo", "eth", "epfl",
]

SCHOOL_DOMAINS = {
    "cmu": ["cmu.edu"],
    "carnegie mellon": ["cmu.edu"],
    "mit": ["mit.edu"],
    "stanford": ["stanford.edu"],
    "berkeley": ["berkeley.edu"],
    "ucsd": ["ucsd.edu"],
    "ucla": ["ucla.edu"],
    "usc": ["usc.edu"],
    "cornell": ["cornell.edu"],
    "columbia": ["columbia.edu"],
    "upenn": ["upenn.edu"],
    "penn": ["upenn.edu"],
    "harvard": ["harvard.edu"],
    "oxford": ["ox.ac.uk"],
    "cambridge": ["cam.ac.uk"],
    "imperial": ["imperial.ac.uk"],
    "ucl": ["ucl.ac.uk"],
    "nus": ["nus.edu.sg"],
    "ntu": ["ntu.edu.sg"],
    "hku": ["hku.hk"],
    "hkust": ["hkust.edu.hk"],
    "cuhk": ["cuhk.edu.hk"],
    "polyu": ["polyu.edu.hk"],
    "cityu": ["cityu.edu.hk"],
    "toronto": ["utoronto.ca"],
    "waterloo": ["uwaterloo.ca"],
    "eth": ["ethz.ch"],
    "epfl": ["epfl.ch"],
}

KNOWN_PROGRAM_URLS = {
    "msaii": ["https://msaii.cs.cmu.edu/"],
}

BLOCKED_DOMAINS = [
    "baidu.com",
    "zhihu.com",
    "cmu.edu.cn",
    "facebook.com",
    "m.me",
    "messenger.com",
    "meta.com",
    "support.microsoft.com",
    "support.google.com",
    "iciba.com",
    "islamicfinder.org",
    "masterelectronics.com",
    "amd.com",
    "chsi.com.cn",
    "diyifanwen.com",
]

RELATED_LINK_TERMS = [
    "apply", "admission", "admissions", "application", "requirements",
    "deadline", "curriculum", "course", "courses", "faculty", "people",
    "program", "degree", "tuition", "faq",
]

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}


@dataclass
class WebSearchResult:
    title: str
    url: str
    snippet: str = ""
    content: str = ""

    def to_dict(self) -> Dict[str, str]:
        return {
            "title": self.title,
            "url": self.url,
            "snippet": self.snippet,
            "content": self.content,
        }


def _contains_ascii_word(text: str, term: str) -> bool:
    pattern = rf"(?<![a-z0-9]){re.escape(term.lower())}(?![a-z0-9])"
    return re.search(pattern, text.lower()) is not None


def should_use_web_search(question: str) -> bool:
    normalized = question.lower()
    for term in APPLICATION_TERMS:
        term_lower = term.lower()
        if term_lower.isascii():
            if _contains_ascii_word(normalized, term_lower):
                return True
            continue
        if term_lower in normalized:
            return True

    # Handles terse prompts such as "CMU MSAII 我的优势是什么".
    return any(_contains_ascii_word(normalized, hint) for hint in SCHOOL_HINTS)


def build_web_search_query(question: str) -> str:
    compact_question = " ".join(str(question or "").split())
    if not compact_question:
        return ""
    lower = compact_question.lower()
    supporting_terms = []
    if not any(term in lower for term in ["official", "官网"]):
        supporting_terms.append("official")
    if not any(term in lower for term in ["admission", "admissions", "录取", "申请"]):
        supporting_terms.append("admissions")
    if not any(term in lower for term in ["requirement", "requirements", "要求"]):
        supporting_terms.append("requirements")
    if not any(term in lower for term in ["curriculum", "课程", "faculty", "教授", "导师"]):
        supporting_terms.extend(["program", "curriculum", "faculty"])
    return (
        f"{compact_question} {' '.join(supporting_terms)}"
    )


def build_web_search_queries(question: str) -> List[str]:
    base_query = build_web_search_query(question)
    compact_question = " ".join(str(question or "").split())
    queries = [base_query]
    if compact_question:
        queries.append(f"{compact_question} official program")
        queries.append(f"{compact_question} admissions requirements")
    for domain in detect_preferred_domains(question):
        queries.append(f"{compact_question} site:{domain} admissions requirements curriculum faculty")
    return [query for index, query in enumerate(queries) if query and query not in queries[:index]]


def detect_preferred_domains(question: str) -> List[str]:
    normalized = question.lower()
    domains: List[str] = []
    for school, school_domains in SCHOOL_DOMAINS.items():
        if school in normalized:
            domains.extend(school_domains)
    return [domain for index, domain in enumerate(domains) if domain not in domains[:index]]


def get_known_program_urls(question: str) -> List[str]:
    normalized = question.lower()
    urls: List[str] = []
    for key, key_urls in KNOWN_PROGRAM_URLS.items():
        if key in normalized:
            urls.extend(key_urls)
    return urls


def _clean_text(text: str, max_chars: int = 2000) -> str:
    text = html.unescape(text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_chars].strip()


def _url_domain(url: str) -> str:
    domain = urlparse(url or "").netloc.lower()
    return domain[4:] if domain.startswith("www.") else domain


def _is_blocked_url(url: str) -> bool:
    domain = _url_domain(url)
    return any(domain == blocked or domain.endswith("." + blocked) for blocked in BLOCKED_DOMAINS)


def _url_matches_domain(url: str, domain: str) -> bool:
    url_domain = _url_domain(url)
    domain = domain.lower()
    domain = domain[4:] if domain.startswith("www.") else domain
    return url_domain == domain or url_domain.endswith("." + domain)


def score_result(result: WebSearchResult, question: str, preferred_domains: List[str]) -> int:
    url = result.url or ""
    if _is_blocked_url(url):
        return -1000

    haystack = f"{result.title} {result.url} {result.snippet}".lower()
    score = 0
    for domain in preferred_domains:
        if _url_matches_domain(url, domain):
            score += 80
    for term in RELATED_LINK_TERMS:
        if term in haystack:
            score += 8
    for token in re.findall(r"[a-z0-9]{3,}", question.lower()):
        if token in haystack:
            score += 4
    if any(marker in _url_domain(url) for marker in [".edu", ".ac.", ".edu."]):
        score += 20
    return score


def should_keep_result(result: WebSearchResult, question: str, preferred_domains: List[str]) -> bool:
    if _is_blocked_url(result.url):
        return False
    if not preferred_domains:
        return score_result(result, question, preferred_domains) > 0
    if any(_url_matches_domain(result.url, domain) for domain in preferred_domains):
        return True
    # Allow non-official pages only if they strongly match the program/query.
    return score_result(result, question, preferred_domains) >= 45


def _unwrap_duckduckgo_url(url: str) -> str:
    url = html.unescape(url or "")
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if "uddg" in query and query["uddg"]:
        return unquote(query["uddg"][0])
    if parsed.path == "/l/" and "uddg=" in url:
        return unquote(url.split("uddg=", 1)[1].split("&", 1)[0])
    return url


class DuckDuckGoResultParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.results: List[WebSearchResult] = []
        self._active_title: List[str] = []
        self._active_snippet: List[str] = []
        self._active_href = ""
        self._last_result: WebSearchResult | None = None
        self._collect_title = False
        self._collect_snippet = False

    def handle_starttag(self, tag: str, attrs) -> None:
        attrs_dict = dict(attrs)
        class_name = attrs_dict.get("class", "")
        if tag == "a" and "result__a" in class_name:
            self._active_href = attrs_dict.get("href", "")
            self._active_title = []
            self._collect_title = True
            return
        if "result__snippet" in class_name and self._last_result is not None:
            self._active_snippet = []
            self._collect_snippet = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._collect_title:
            title = _clean_text(" ".join(self._active_title), 280)
            url = _unwrap_duckduckgo_url(self._active_href)
            if title and url.startswith(("http://", "https://")):
                self._last_result = WebSearchResult(title=title, url=url)
                self.results.append(self._last_result)
            self._collect_title = False
            self._active_href = ""
            self._active_title = []
            return
        if self._collect_snippet and tag in {"a", "div"}:
            if self._last_result is not None:
                self._last_result.snippet = _clean_text(" ".join(self._active_snippet), 600)
            self._collect_snippet = False
            self._active_snippet = []

    def handle_data(self, data: str) -> None:
        if self._collect_title:
            self._active_title.append(data)
        elif self._collect_snippet:
            self._active_snippet.append(data)


class VisibleTextParser(HTMLParser):
    SKIP_TAGS = {"script", "style", "noscript", "svg", "canvas", "form", "nav", "footer"}

    def __init__(self) -> None:
        super().__init__()
        self.parts: List[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in self.SKIP_TAGS:
            self._skip_depth += 1
            return
        if tag in {"title", "h1", "h2", "h3", "p", "li", "dt", "dd"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in self.SKIP_TAGS and self._skip_depth:
            self._skip_depth -= 1
            return
        if tag in {"title", "h1", "h2", "h3", "p", "li", "dt", "dd"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return
        text = data.strip()
        if text:
            self.parts.append(text)

    def text(self) -> str:
        return _clean_text(" ".join(self.parts), 2400)


def duckduckgo_search(query: str, max_results: int = WEB_SEARCH_MAX_RESULTS) -> List[WebSearchResult]:
    if not query:
        return []
    response = requests.get(
        "https://duckduckgo.com/html/",
        params={"q": query, "kl": "us-en"},
        headers=REQUEST_HEADERS,
        timeout=WEB_SEARCH_TIMEOUT,
    )
    response.raise_for_status()
    parser = DuckDuckGoResultParser()
    parser.feed(response.text)

    results: List[WebSearchResult] = []
    seen = set()
    for result in parser.results:
        if result.url in seen:
            continue
        seen.add(result.url)
        results.append(result)
        if len(results) >= max_results:
            break
    return results


def bing_search(query: str, max_results: int = WEB_SEARCH_MAX_RESULTS) -> List[WebSearchResult]:
    if not query:
        return []
    response = requests.get(
        "https://www.bing.com/search",
        params={"q": query, "setlang": "en-us", "mkt": "en-US", "cc": "US"},
        headers=REQUEST_HEADERS,
        timeout=WEB_SEARCH_TIMEOUT,
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    results: List[WebSearchResult] = []
    seen = set()
    for item in soup.select("li.b_algo"):
        link = item.find("a", href=True)
        if not link:
            continue
        url = link.get("href", "")
        title = _clean_text(link.get_text(" ", strip=True), 280)
        snippet_node = item.select_one(".b_caption p") or item.find("p")
        snippet = _clean_text(snippet_node.get_text(" ", strip=True) if snippet_node else "", 600)
        if not title or not url.startswith(("http://", "https://")) or url in seen:
            continue
        seen.add(url)
        results.append(WebSearchResult(title=title, url=url, snippet=snippet))
        if len(results) >= max_results:
            break
    return results


def fetch_page_html(url: str) -> str:
    response = requests.get(
        url,
        headers=REQUEST_HEADERS,
        timeout=WEB_SEARCH_TIMEOUT,
        allow_redirects=True,
    )
    response.raise_for_status()
    content_type = response.headers.get("content-type", "").lower()
    if "text/html" not in content_type:
        return ""
    return response.text


def extract_visible_text(html_text: str) -> str:
    parser = VisibleTextParser()
    parser.feed(html_text)
    return parser.text()


def fetch_page_text(url: str) -> str:
    html_text = fetch_page_html(url)
    if not html_text:
        return ""
    return extract_visible_text(html_text)


def discover_related_links(url: str, html_text: str, max_links: int = 4) -> List[str]:
    if not html_text:
        return []
    base_domain = _url_domain(url)
    soup = BeautifulSoup(html_text, "html.parser")
    candidates = []
    seen = set()
    for link in soup.find_all("a", href=True):
        href = urljoin(url, link.get("href", ""))
        parsed = urlparse(href)
        if parsed.scheme not in {"http", "https"}:
            continue
        href = parsed._replace(fragment="").geturl()
        if href in seen or _url_domain(href) != base_domain:
            continue
        text = f"{link.get_text(' ', strip=True)} {href}".lower()
        if not any(term in text for term in RELATED_LINK_TERMS):
            continue
        seen.add(href)
        score = sum(1 for term in RELATED_LINK_TERMS if term in text)
        candidates.append((score, href))
    candidates.sort(reverse=True)
    return [href for _, href in candidates[:max_links]]


def search_web(question: str) -> Dict[str, object]:
    queries = build_web_search_queries(question)
    query = queries[0] if queries else ""
    bundle: Dict[str, object] = {
        "query": query,
        "queries": queries,
        "results": [],
        "error": "",
    }
    if not query:
        return bundle

    try:
        preferred_domains = detect_preferred_domains(question)
        result_by_url: Dict[str, WebSearchResult] = {}
        for known_url in get_known_program_urls(question):
            result_by_url[known_url] = WebSearchResult(
                title=f"Official program page: {_url_domain(known_url)}",
                url=known_url,
            )

        for current_query in queries:
            current_results: List[WebSearchResult] = []
            try:
                current_results.extend(bing_search(current_query, WEB_SEARCH_MAX_RESULTS))
            except Exception:
                pass
            if not current_results:
                try:
                    current_results.extend(duckduckgo_search(current_query, WEB_SEARCH_MAX_RESULTS))
                except Exception:
                    pass
            for result in current_results:
                if not result.url or _is_blocked_url(result.url):
                    continue
                if result.url not in result_by_url:
                    result_by_url[result.url] = result

        results = list(result_by_url.values())
        results.sort(
            key=lambda result: score_result(result, question, preferred_domains),
            reverse=True,
        )
        results = [
            result for result in results
            if should_keep_result(result, question, preferred_domains)
        ][:WEB_SEARCH_MAX_RESULTS]

        enriched: List[Dict[str, str]] = []
        extra_urls: List[str] = []
        seen_urls = {result.url for result in results}
        for index, result in enumerate(results):
            if index < WEB_SEARCH_MAX_PAGES:
                try:
                    html_text = fetch_page_html(result.url)
                    result.content = extract_visible_text(html_text)
                    for href in discover_related_links(result.url, html_text):
                        if href not in seen_urls and not _is_blocked_url(href):
                            seen_urls.add(href)
                            extra_urls.append(href)
                except Exception:
                    result.content = ""
            enriched.append(result.to_dict())

        for href in extra_urls[:max(0, WEB_SEARCH_MAX_RESULTS - len(enriched))]:
            try:
                content = fetch_page_text(href)
            except Exception:
                content = ""
            enriched.append(
                WebSearchResult(
                    title=f"Related official page: {_url_domain(href)}",
                    url=href,
                    content=content,
                ).to_dict()
            )
        bundle["results"] = enriched
    except Exception as exc:
        bundle["error"] = str(exc)
    return bundle


def search_url_for_query(query: str) -> str:
    return f"https://duckduckgo.com/?q={quote_plus(query)}"
