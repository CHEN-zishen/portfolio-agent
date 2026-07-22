import shutil
import time
import unicodedata
import os
import re
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, List, Optional
from html import escape
from urllib.parse import quote

os.environ.setdefault("PATH", os.environ.get("Path", ""))

import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

from .config import (
    BASE_DIR,
    CATEGORY_LABEL_BY_DIR,
    CHROMA_DIR,
    COLLECTION_NAME,
    DATA_DIR,
    DOCS_DIR,
    EMBEDDING_MODEL,
    SUPPORTED_SUFFIXES,
    get_setting,
)
from .data import SYSTEM_PROMPT
from .web_search import search_web, should_use_web_search

class StreamHandler(BaseCallbackHandler):
    """Write streamed LLM tokens into a Streamlit placeholder."""

    def __init__(self, container):
        self.container = container
        self.text = ""

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text + "▌")


@st.cache_resource(show_spinner=False)
def ensure_docs_structure() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    for folder in CATEGORY_LABEL_BY_DIR:
        (DOCS_DIR / folder).mkdir(parents=True, exist_ok=True)


def get_embeddings() -> HuggingFaceEmbeddings:
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def get_vectorstore() -> Chroma:
    ensure_docs_structure()
    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
        embedding_function=get_embeddings(),
    )


def iter_source_files() -> Iterable[Path]:
    seen = set()
    for folder in CATEGORY_LABEL_BY_DIR:
        current_dir = DOCS_DIR / folder
        if not current_dir.exists():
            continue
        for path in current_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES:
                seen.add(path.resolve())
                yield path
    if not DATA_DIR.exists():
        return
    for path in DATA_DIR.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        yield path


def infer_category_from_path(path: Path) -> str:
    """Map docs and data paths to the assistant's existing navigation filters."""
    try:
        relative_docs = path.relative_to(DOCS_DIR)
        return relative_docs.parts[0] if relative_docs.parts else "portfolio"
    except ValueError:
        pass

    try:
        relative_data = path.relative_to(DATA_DIR)
    except ValueError:
        return "portfolio"

    if not relative_data.parts:
        return "portfolio"

    top_level = relative_data.parts[0].lower()
    if top_level in {"research", "research_thumbs"}:
        return "papers"
    if top_level in {"competition awards", "aesthetic education"}:
        return "competition"
    if top_level == "websites and systems":
        return "projects"
    if top_level == "resume":
        return "resume"
    return "portfolio"


def _relative_path_text(path: Path) -> str:
    try:
        return str(path.relative_to(BASE_DIR))
    except ValueError:
        return str(path)


def _format_structured_key(key: object) -> str:
    return str(key).replace("_", " ").strip().title()


def _stringify_structured_value(value: object, indent: int = 0) -> str:
    prefix = " " * indent
    if value is None:
        return ""
    if isinstance(value, Path):
        suffix = value.suffix.lower()
        if suffix in SUPPORTED_SUFFIXES:
            return f"Evidence file: {_relative_path_text(value)}"
        return ""
    if isinstance(value, dict):
        lines = []
        for key, child in value.items():
            child_text = _stringify_structured_value(child, indent + 2)
            if not child_text:
                continue
            label = _format_structured_key(key)
            if "\n" in child_text:
                lines.append(f"{prefix}{label}:\n{child_text}")
            else:
                lines.append(f"{prefix}{label}: {child_text}")
        return "\n".join(lines)
    if isinstance(value, (list, tuple, set)):
        lines = []
        for child in value:
            child_text = _stringify_structured_value(child, indent + 2)
            if not child_text:
                continue
            child_text = child_text.replace("\n", "\n" + prefix + "  ")
            lines.append(f"{prefix}- {child_text}")
        return "\n".join(lines)
    return f"{value}"


def _structured_document(
    *,
    category: str,
    source: str,
    title: str,
    content: object,
    item_id: str = "",
    extra_metadata: Optional[Dict[str, object]] = None,
) -> Document:
    category_label = CATEGORY_LABEL_BY_DIR.get(category, "Full Portfolio")
    body = _stringify_structured_value(content)
    page_content = (
        f"Portfolio app page text\n"
        f"Section: {category_label}\n"
        f"Title: {title}\n"
        f"{body}"
    )
    metadata = {
        "category": category,
        "category_label": category_label,
        "source": source,
        "filename": "portfolio_app/data.py",
        "item_id": item_id,
        "title": title,
        "structured": True,
    }
    if extra_metadata:
        metadata.update(extra_metadata)

    return Document(
        page_content=page_content,
        metadata=metadata,
    )


def load_structured_portfolio_documents() -> List[Document]:
    from .data import (
        COMPETITION_AWARDS,
        INTERNSHIPS,
        INTERNSHIP_EXPERIENCES,
        MAIN_COURSES,
        PERSONAL_INFO,
        PRACTICES,
        PROJECTS,
        RESEARCH_DIRECTIONS,
        RESEARCH_PAPERS,
        RESUME_SECTIONS,
    )

    documents: List[Document] = []
    section_intros = [
        (
            "papers",
            "portfolio_app/research.py::section_intro",
            "Research Papers page overview",
            "Research works organized as explorable project stories. Choose a paper to enter a focused detail page with paper screenshots, experimental figures, tables, and an interview-ready explanation of the work.",
        ),
        (
            "competition",
            "portfolio_app/competitions.py::section_intro",
            "Competitions & Awards page overview",
            "Competitive achievements and recognitions, including competition awards, scholarships, sports recognitions, project overview, methodology, award information, achievements, and certificate evidence.",
        ),
        (
            "projects",
            "portfolio_app/projects.py::section_intro",
            "Engineering Projects page overview",
            "Showcase of software engineering and AI development projects. Detail pages include tech stack, architecture, features, implementation highlights, outcomes, and GitHub links where available.",
        ),
        (
            "resume",
            "portfolio_app/internships.py::section_intro",
            "Internships & Practices page overview",
            "Professional internships, campus practices, role overview, key achievements, skills gained, period, location, tags, and supporting document previews.",
        ),
    ]
    for category, source, title, content in section_intros:
        documents.append(
            _structured_document(category=category, source=source, title=title, content=content)
        )

    profile_content = {
        "personal_info": PERSONAL_INFO,
        "main_courses": MAIN_COURSES,
        "research_directions": RESEARCH_DIRECTIONS,
        "homepage_internship_highlights": INTERNSHIP_EXPERIENCES,
        "resume_sections": RESUME_SECTIONS,
    }
    documents.append(
        _structured_document(
            category="portfolio",
            source="portfolio_app/data.py::PROFILE",
            title="Homepage profile, courses, research directions, and resume summary",
            content=profile_content,
        )
    )

    research_summary_items = [
        {
            "id": paper.get("id"),
            "title": paper.get("title"),
            "tag": paper.get("tag"),
            "venue": paper.get("venue"),
            "summary": paper.get("summary"),
            "highlights": paper.get("highlights", []),
        }
        for paper in RESEARCH_PAPERS
    ]
    documents.append(
        _structured_document(
            category="papers",
            source="portfolio_app/data.py::RESEARCH_PAPERS_SUMMARY",
            title="Research Papers summary and total count",
            content={
                "total_research_papers": len(RESEARCH_PAPERS),
                "statement": f"The Research Papers section contains {len(RESEARCH_PAPERS)} papers.",
                "papers": research_summary_items,
            },
            extra_metadata={"summary_kind": "research_papers_count"},
        )
    )

    award_groups: Dict[str, List[Dict]] = {}
    for award in COMPETITION_AWARDS:
        award_groups.setdefault(str(award.get("category", "Other")), []).append(award)
    for award_category, awards in sorted(award_groups.items()):
        summary_items = []
        for award in sorted(awards, key=lambda item: (-int(item.get("year", 0)), item.get("title", ""))):
            summary_items.append(
                {
                    "id": award.get("id"),
                    "title": award.get("title"),
                    "category": award.get("category"),
                    "level": award.get("level"),
                    "year": award.get("year"),
                    "description": award.get("description"),
                    "achievements": award.get("achievements", []),
                    "tags": award.get("tags", []),
                }
            )
        documents.append(
            _structured_document(
                category="competition",
                source=f"portfolio_app/data.py::COMPETITION_AWARDS_CATEGORY/{award_category}",
                title=f"Competitions & Awards - {award_category} category",
                content={
                    "category_filter": award_category,
                    "count": len(summary_items),
                    "items": summary_items,
                },
                extra_metadata={"award_category": award_category},
            )
        )

    collections = [
        ("papers", "RESEARCH_PAPERS", RESEARCH_PAPERS, "title"),
        ("competition", "COMPETITION_AWARDS", COMPETITION_AWARDS, "title"),
        ("projects", "PROJECTS", PROJECTS, "title"),
        ("resume", "INTERNSHIPS", INTERNSHIPS, "company"),
        ("resume", "PRACTICES", PRACTICES, "organization"),
    ]
    for category, collection_name, records, title_key in collections:
        for index, record in enumerate(records, start=1):
            item_id = str(record.get("id", index))
            title = str(record.get(title_key) or record.get("title") or item_id)
            documents.append(
                _structured_document(
                    category=category,
                    source=f"portfolio_app/data.py::{collection_name}/{item_id}",
                    title=title,
                    content=record,
                    item_id=item_id,
                    extra_metadata={"award_category": record.get("category")} if collection_name == "COMPETITION_AWARDS" else None,
                )
            )
    return documents


def _iter_supported_paths(value: object) -> Iterable[Path]:
    if isinstance(value, Path):
        if value.suffix.lower() in SUPPORTED_SUFFIXES:
            yield value
        return
    if isinstance(value, dict):
        for child in value.values():
            yield from _iter_supported_paths(child)
        return
    if isinstance(value, (list, tuple, set)):
        for child in value:
            yield from _iter_supported_paths(child)


def get_portfolio_item_metadata_for_path(path: Path) -> Dict[str, str]:
    from .data import (
        COMPETITION_AWARDS,
        INTERNSHIPS,
        PRACTICES,
        PROJECTS,
        RESEARCH_PAPERS,
    )

    collections = [
        ("papers", RESEARCH_PAPERS, "title"),
        ("competition", COMPETITION_AWARDS, "title"),
        ("projects", PROJECTS, "title"),
        ("resume", INTERNSHIPS, "company"),
        ("resume", PRACTICES, "organization"),
    ]
    path = path.resolve()
    resolved_path = path
    for category, records, title_key in collections:
        for index, record in enumerate(records, start=1):
            item_paths = {item_path.resolve() for item_path in _iter_supported_paths(record)}
            if resolved_path not in item_paths:
                continue
            item_id = str(record.get("id", index))
            title = str(record.get(title_key) or record.get("title") or item_id)
            return {"category": category, "item_id": item_id, "title": title}
    return {}


def get_document_metadata_for_path(path: Path, category: str) -> Dict[str, str]:
    path = path.resolve()
    try:
        relative_docs = path.relative_to(DOCS_DIR)
    except ValueError:
        return {}

    relative_text = str(relative_docs).replace("\\", "/").lower()
    if category == "competition" and "sports" in relative_text:
        return {
            "award_category": "Sports",
            "title": "Competitions & Awards - Sports",
        }
    if category == "competition" and "scholarship" in relative_text:
        return {
            "award_category": "Scholarship",
            "title": "Competitions & Awards - Scholarship",
        }
    return {}


def load_one_file(path: Path) -> List[Document]:
    path = path.resolve()
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        docs = PyPDFLoader(str(path)).load()
    else:
        docs = TextLoader(str(path), encoding="utf-8").load()

    item_metadata = get_portfolio_item_metadata_for_path(path)
    folder = item_metadata.get("category") or infer_category_from_path(path)
    document_metadata = get_document_metadata_for_path(path, folder)
    for doc in docs:
        metadata = {
            "category": folder,
            "category_label": CATEGORY_LABEL_BY_DIR.get(folder, "Full Portfolio"),
            "source": str(path.relative_to(BASE_DIR)),
            "filename": path.name,
        }
        metadata.update(document_metadata)
        metadata.update(item_metadata)
        doc.metadata.update(metadata)
    return docs


def clean_text_for_embedding(text: object) -> str:
    """Normalize document text and remove invisible chars that break tokenizers."""
    if text is None:
        return ""
    if not isinstance(text, str):
        text = str(text)
    text = unicodedata.normalize("NFKC", text)
    text = "".join(
        char if unicodedata.category(char)[0] != "C" or char in "\n\t" else " "
        for char in text
    )
    return " ".join(text.split())


def load_all_documents() -> List[Document]:
    documents: List[Document] = []
    documents.extend(load_structured_portfolio_documents())
    for path in iter_source_files():
        try:
            documents.extend(load_one_file(path))
        except Exception as exc:
            st.warning(f"Failed to load file: {path.name}. Reason: {exc}")
    cleaned_documents: List[Document] = []
    for doc in documents:
        content = clean_text_for_embedding(doc.page_content)
        if not content:
            continue
        doc.page_content = content
        cleaned_documents.append(doc)
    return cleaned_documents


def rebuild_vectorstore() -> int:
    if CHROMA_DIR.exists():
        shutil.rmtree(CHROMA_DIR)

    raw_docs = load_all_documents()
    if not raw_docs:
        get_vectorstore()
        return 0

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=140,
        separators=["\n\n", "\n", "。", "；", ";", ".", " ", ""],
    )
    chunks = splitter.split_documents(raw_docs)
    cleaned_chunks: List[Document] = []
    for chunk in chunks:
        content = clean_text_for_embedding(chunk.page_content)
        if not content:
            continue
        chunk.page_content = content
        cleaned_chunks.append(chunk)
    chunks = cleaned_chunks
    Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_DIR),
    )
    return len(chunks)


@st.cache_resource(show_spinner=False)
def ensure_vectorstore_ready() -> Dict[str, object]:
    status = get_vectorstore_status()
    if status.get("ready"):
        return status

    chunk_count = rebuild_vectorstore()
    try:
        get_vectorstore_status.clear()
    except Exception:
        pass
    status = get_vectorstore_status()
    status["rebuilt"] = True
    status["chunks"] = chunk_count
    return status


def format_docs(docs: List[Document]) -> str:
    if not docs:
        return ""
    formatted = []
    for idx, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        category = doc.metadata.get("category_label", "unknown")
        formatted.append(
            f"[Chunk {idx} | Section: {category} | Source: {source}]\n{doc.page_content}"
        )
    return "\n\n".join(formatted)


def format_web_context(web_bundle: Optional[Dict[str, object]]) -> str:
    if not web_bundle:
        return ""
    results = web_bundle.get("results") or []
    if not isinstance(results, list):
        return ""

    formatted = []
    for idx, result in enumerate(results, start=1):
        if not isinstance(result, dict):
            continue
        title = str(result.get("title") or "Untitled").strip()
        url = str(result.get("url") or "").strip()
        snippet = str(result.get("snippet") or "").strip()
        content = str(result.get("content") or "").strip()
        body = content or snippet
        if not url or not body:
            continue
        formatted.append(
            f"[Web {idx} | Title: {title} | URL: {url}]\n{body[:2200]}"
        )
    return "\n\n".join(formatted)


def format_web_source_links(web_bundle: Optional[Dict[str, object]], language: str) -> str:
    if not web_bundle:
        return ""
    results = web_bundle.get("results") or []
    if not isinstance(results, list):
        return ""

    links = []
    seen = set()
    for result in results:
        if not isinstance(result, dict):
            continue
        url = str(result.get("url") or "").strip()
        title = str(result.get("title") or url).strip()
        if not url or url in seen:
            continue
        seen.add(url)
        links.append((title, url))
        if len(links) >= 4:
            break

    if not links:
        return ""

    heading = "联网检索来源：" if language == "Chinese" else "Web search sources:"
    items = "".join(
        f'<li><a href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(title)}</a></li>'
        for title, url in links
    )
    return f'\n\n<div class="web-answer-sources"><p>{heading}</p><ul>{items}</ul></div>'


def compact_match_text(value: object) -> str:
    normalized = unicodedata.normalize("NFKC", str(value or "")).lower()
    return "".join(char for char in normalized if char.isalnum())


def document_item_key(doc: Document) -> Optional[tuple]:
    category = doc.metadata.get("category")
    item_id = doc.metadata.get("item_id")
    if not category or not item_id:
        return None
    return category, str(item_id)


def get_mentioned_portfolio_item_keys(question: str, docs: List[Document]) -> set:
    normalized_question = compact_match_text(question)
    if not normalized_question:
        return set()

    mentioned = set()
    for doc in docs:
        key = document_item_key(doc)
        if not key:
            continue
        candidates = [
            doc.metadata.get("item_id"),
            doc.metadata.get("title"),
        ]
        for candidate in candidates:
            candidate_text = compact_match_text(candidate)
            if len(candidate_text) < 4:
                continue
            if candidate_text in normalized_question:
                mentioned.add(key)
                break
    return mentioned


def contains_any_query_term(text: str, terms: List[str]) -> bool:
    normalized = text.lower()
    for term in terms:
        if not term:
            continue
        term_lower = term.lower()
        if term_lower.isascii() and any(char.isalnum() for char in term_lower):
            pattern = rf"(?<![a-z0-9]){re.escape(term_lower)}(?![a-z0-9])"
            if re.search(pattern, normalized):
                return True
            continue
        if term_lower in normalized:
            return True
    return False


def get_allowed_link_categories(question: str) -> Optional[set]:
    category_terms = {
        "papers": ["论文", "文章", "paper", "papers", "research papers"],
        "projects": ["项目", "project", "系统", "工程", "ventureagent", "socialdiffusion", "puzzlesolver"],
        "competition": ["比赛", "竞赛", "奖项", "获奖", "飞盘", "体育", "competition", "award", "sports", "frisbee"],
        "resume": ["实习", "实践", "经历", "internship", "practice"],
    }
    allowed = {
        category for category, terms in category_terms.items()
        if contains_any_query_term(question, terms)
    }
    return allowed or None


def format_portfolio_links(docs: List[Document], language: str, question: str = "") -> str:
    link_params = {
        "papers": "paper",
        "competition": "competition",
        "projects": "project",
        "resume": "internship",
    }
    allowed_categories = get_allowed_link_categories(question) if question else None
    mentioned_item_keys = get_mentioned_portfolio_item_keys(question, docs) if question else set()
    links = []
    seen = set()
    for doc in docs:
        category = doc.metadata.get("category")
        if allowed_categories is not None and category not in allowed_categories:
            continue
        item_id = doc.metadata.get("item_id")
        item_key = document_item_key(doc)
        if mentioned_item_keys and item_key not in mentioned_item_keys:
            continue
        param = link_params.get(category)
        award_category = doc.metadata.get("award_category")
        source = doc.metadata.get("source", "")
        if category == "competition" and award_category and "COMPETITION_AWARDS_CATEGORY" in source:
            key = ("competition_category", award_category)
            if key in seen:
                continue
            seen.add(key)
            title = f"Competitions & Awards - {award_category}"
            links.append((title, f"?competition_category={quote(str(award_category))}"))
            continue
        if not param or not item_id:
            continue
        key = (param, item_id)
        if key in seen:
            continue
        seen.add(key)
        title = doc.metadata.get("title") or doc.metadata.get("source") or item_id
        links.append((str(title), f"?{param}={quote(str(item_id))}"))
        if len(links) >= 4:
            break

    if not links:
        return ""

    heading = "相关作品集入口：" if language == "Chinese" else "Related portfolio links:"
    items = "".join(
        f'<li><a href="{escape(href, quote=True)}" target="_self">{escape(title)}</a></li>'
        for title, href in links
    )
    return f'\n\n<div class="portfolio-answer-links"><p>{heading}</p><ul>{items}</ul></div>'


def format_research_paper_count_answer(language: str) -> str:
    from .data import RESEARCH_PAPERS

    items = "".join(
        f'<li><a href="?paper={quote(str(paper["id"]))}" target="_self">{escape(str(paper["title"]))}</a></li>'
        for paper in RESEARCH_PAPERS
    )
    if language == "Chinese":
        return (
            f'Research Papers 里目前共有 <strong>{len(RESEARCH_PAPERS)}</strong> 篇论文。'
            f'\n\n<div class="portfolio-answer-links"><p>相关作品集入口：</p><ul>{items}</ul></div>'
        )
    return (
        f'The Research Papers section currently contains <strong>{len(RESEARCH_PAPERS)}</strong> papers.'
        f'\n\n<div class="portfolio-answer-links"><p>Related portfolio links:</p><ul>{items}</ul></div>'
    )


def get_current_date_context() -> Dict[str, object]:
    today = date.today()
    weekday_en = today.strftime("%A")
    weekday_zh = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"][today.weekday()]
    return {
        "today": today,
        "iso": today.isoformat(),
        "year": today.year,
        "weekday_en": weekday_en,
        "weekday_zh": weekday_zh,
    }


def calculate_age(birth_date: date, today: date) -> int:
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def get_direct_time_or_age_answer(question: str, language: str) -> str:
    current = get_current_date_context()
    today = current["today"]
    birth_date = date(2004, 7, 26)
    age = calculate_age(birth_date, today)

    asks_age = contains_any_query_term(question, ["年龄", "几岁", "多大", "age", "old"])
    asks_birthday = contains_any_query_term(question, ["生日", "出生", "birth", "birthday", "date of birth"])
    asks_today = contains_any_query_term(question, ["今天", "today", "当前日期", "日期"])
    asks_weekday = contains_any_query_term(question, ["星期几", "周几", "weekday", "day of week"])
    asks_year = contains_any_query_term(question, ["今年", "年份", "year"])

    if asks_age:
        if language == "Chinese":
            return (
                f"按今天 {current['iso']}（{current['weekday_zh']}）计算，"
                f"我的出生日期是 2004 年 7 月 26 日，所以我今年 {age} 岁。"
            )
        return (
            f"As of today, {current['iso']} ({current['weekday_en']}), "
            f"I am {age} years old based on my date of birth, July 26, 2004."
        )

    if asks_birthday:
        if language == "Chinese":
            return "我的出生日期是 2004 年 7 月 26 日。"
        return "My date of birth is July 26, 2004."

    if asks_today or asks_weekday or asks_year:
        if language == "Chinese":
            return f"今天是 {current['iso']}，{current['weekday_zh']}，年份是 {current['year']} 年。"
        return f"Today is {current['iso']}, {current['weekday_en']}. The year is {current['year']}."

    return ""


def get_direct_profile_answer(question: str, language: str) -> str:
    from .data import PERSONAL_INFO

    direct_time_answer = get_direct_time_or_age_answer(question, language)
    if direct_time_answer:
        return direct_time_answer

    profile_fields = [
        ("Major", ["专业", "major"], "我的专业是", "My major is"),
        ("University", ["学校", "大学", "university", "school"], "我就读于", "I study at"),
        ("GPA", ["gpa", "绩点"], "我的 GPA 是", "My GPA is"),
        ("Academic Ranking", ["排名", "ranking"], "我的学业排名是", "My academic ranking is"),
        ("Name", ["姓名", "名字", "name"], "我的名字是", "My name is"),
        ("Date of Birth", ["出生日期", "date of birth"], "我的出生日期是", "My date of birth is"),
        ("Research Interests", ["研究方向", "research interests"], "我的研究方向包括", "My research interests include"),
        ("Technical Stack", ["技术栈", "技能", "technical stack"], "我的技术栈包括", "My technical stack includes"),
        ("Career Goal", ["职业目标", "career goal"], "我的职业目标是", "My career goal is"),
    ]
    for field, terms, chinese_prefix, english_prefix in profile_fields:
        if not contains_any_query_term(question, terms):
            continue
        value = PERSONAL_INFO.get(field)
        if not value:
            continue
        if language == "Chinese":
            return f"{chinese_prefix} {value}。"
        return f"{english_prefix} {value}."
    return ""


def should_show_portfolio_links(question: str, docs: List[Document]) -> bool:
    link_intent_terms = [
        "论文", "文章", "paper", "research papers", "项目", "project", "系统", "工程",
        "比赛", "竞赛", "奖项", "获奖", "飞盘", "体育", "competition", "award",
        "实习", "实践", "经历", "internship", "practice", "详情", "detail",
        "链接", "入口", "跳转", "作品", "portfolio", "view",
    ]
    has_link_intent = contains_any_query_term(question, link_intent_terms)
    mentioned_item_keys = get_mentioned_portfolio_item_keys(question, docs)

    personal_info_terms = [
        "性别", "年龄", "生日", "出生", "籍贯", "电话", "邮箱", "email", "phone",
        "gpa", "绩点", "排名", "学校", "大学", "专业", "名字", "姓名",
        "gender", "age", "birthday", "birth", "hometown", "name", "university", "major",
    ]
    if contains_any_query_term(question, personal_info_terms) and not has_link_intent and not mentioned_item_keys:
        return False

    if has_link_intent:
        return True

    return bool(mentioned_item_keys)


def should_focus_competition_awards(question: str, category_dir: Optional[str]) -> bool:
    normalized = question.lower()
    asks_competition = any(term in normalized for term in ["比赛", "竞赛", "competition", "contest"])
    excludes_competition = any(term in normalized for term in ["飞盘", "体育", "运动", "sports", "frisbee", "scholarship", "奖学金"])
    if not asks_competition or excludes_competition:
        return False
    return category_dir in (None, "competition")


def should_focus_sports_awards(question: str, category_dir: Optional[str]) -> bool:
    normalized = question.lower()
    asks_sports = any(term in normalized for term in ["飞盘", "体育", "运动", "sports", "frisbee", "athletic"])
    return asks_sports and category_dir in (None, "competition")


def should_focus_research_paper_count(question: str, category_dir: Optional[str]) -> bool:
    normalized = question.lower()
    asks_papers = any(term in normalized for term in ["论文", "paper", "papers", "文章", "research papers"])
    asks_count = any(term in normalized for term in ["几篇", "多少篇", "总共", "一共", "数量", "count", "how many"])
    return asks_papers and asks_count and category_dir in (None, "papers")


def should_focus_profile_info(question: str, category_dir: Optional[str]) -> bool:
    profile_terms = [
        "专业", "学校", "大学", "gpa", "绩点", "排名", "姓名", "名字", "研究方向",
        "技术栈", "职业目标", "课程", "major", "university", "school", "ranking",
        "name", "research interests", "technical stack", "career goal", "courses",
    ]
    return category_dir is None and contains_any_query_term(question, profile_terms)


def should_focus_volunteer_experience(question: str, category_dir: Optional[str]) -> bool:
    volunteer_terms = [
        "志愿", "义工", "公益", "社区", "服务", "清洁海岸", "保护家园", "垃圾清扫",
        "心肺复苏", "cpr", "急救", "相约蓝天", "潮服会", "银龄", "非遗",
        "关爱老人", "暖冬护绿", "青马同行", "宣传片", "毕业晚会", "迎新",
        "文明引导", "宿舍清扫", "电梯秩序", "volunteer", "public service",
        "community service", "coastal cleanup", "first aid", "elderly care",
    ]
    return category_dir in (None, "resume") and contains_any_query_term(question, volunteer_terms)


def should_focus_large_model_work(question: str, category_dir: Optional[str]) -> bool:
    large_model_terms = [
        "大模型", "基础模型", "生成式", "生成模型", "多模态", "视觉大模型", "医学大模型",
        "大语言模型", "llm", "large language model", "large model", "foundation model",
        "generative ai", "diffusion", "latent diffusion", "stable diffusion", "lora",
        "mamba", "transformer", "vision transformer", "multimodal",
    ]
    role_terms = [
        "工程师", "研究员", "岗位", "职位", "申请", "优势", "匹配", "适合", "能不能",
        "engineer", "researcher", "role", "job", "fit", "advantage", "application",
    ]
    work_terms = [
        "工作", "论文", "研究", "项目", "经历", "能力", "背景", "方向", "文章",
        "work", "paper", "research", "project", "experience", "background",
    ]
    if category_dir not in (None, "papers", "projects", "resume"):
        return False
    return contains_any_query_term(question, large_model_terms) and (
        contains_any_query_term(question, role_terms)
        or contains_any_query_term(question, work_terms)
        or category_dir in ("papers", "projects", "resume")
    )


def _dedupe_documents(docs: List[Document]) -> List[Document]:
    seen = set()
    unique_docs = []
    for doc in docs:
        if doc.metadata.get("summary_kind"):
            key = (doc.metadata.get("source"), doc.metadata.get("summary_kind"))
        elif "COMPETITION_AWARDS_CATEGORY" in doc.metadata.get("source", ""):
            key = (doc.metadata.get("source"), doc.metadata.get("award_category"))
        else:
            key = (
                doc.metadata.get("source"),
                doc.metadata.get("item_id"),
                doc.page_content[:160],
            )
        if key in seen:
            continue
        seen.add(key)
        unique_docs.append(doc)
    return unique_docs


def get_documents_by_source(vectorstore: Chroma, sources: List[str], limit_per_source: int = 2) -> List[Document]:
    docs: List[Document] = []
    for source in sources:
        try:
            results = vectorstore.get(
                where={"source": source},
                include=["documents", "metadatas"],
                limit=limit_per_source,
            )
        except Exception:
            continue
        documents = results.get("documents") or []
        metadatas = results.get("metadatas") or []
        for page_content, metadata in zip(documents, metadatas):
            docs.append(Document(page_content=page_content or "", metadata=metadata or {}))
    return docs


def retrieve_context(question: str, category_dir: Optional[str], top_k: int) -> List[Document]:
    vectorstore = get_vectorstore()
    if should_focus_large_model_work(question, category_dir):
        focused_query = (
            f"{question} diffusion latent diffusion LoRA Mamba Transformer multimodal medical image generation "
            "ScolioLDM Surgi-Diff G2Net VentureAgent DeepSeek LLM"
        )
        paper_docs = vectorstore.similarity_search(
            focused_query,
            k=max(top_k * 3, 14),
            filter={"category": "papers"},
        )
        project_docs = vectorstore.similarity_search(
            focused_query,
            k=max(top_k, 6),
            filter={"category": "projects"},
        )
        resume_docs = vectorstore.similarity_search(
            focused_query,
            k=max(top_k, 6),
            filter={"category": "resume"},
        )
        profile_docs = vectorstore.similarity_search(
            focused_query,
            k=3,
            filter={"source": "portfolio_app/data.py::PROFILE"},
        )
        anchor_docs = get_documents_by_source(
            vectorstore,
            [
                "portfolio_app/data.py::RESEARCH_PAPERS/scolioldm",
                "portfolio_app/data.py::RESEARCH_PAPERS/g2net",
                "portfolio_app/data.py::RESEARCH_PAPERS/smo_diff",
                "portfolio_app/data.py::RESEARCH_PAPERS/surgidiff",
                "portfolio_app/data.py::PROJECTS/venture_agent",
                "portfolio_app/data.py::PROJECTS/social_diffusion",
                "portfolio_app/data.py::INTERNSHIPS/hku",
            ],
            limit_per_source=1,
        )
        balanced_docs = (
            anchor_docs
            + paper_docs[:4]
            + project_docs[:3]
            + resume_docs[:3]
            + profile_docs
            + paper_docs[4:]
            + project_docs[3:]
            + resume_docs[3:]
        )
        return _dedupe_documents(balanced_docs)[:max(top_k, 10)]

    if should_focus_volunteer_experience(question, category_dir):
        volunteer_docs = vectorstore.similarity_search(
            question,
            k=max(top_k * 2, 12),
            filter={"source": "portfolio_app/data.py::PRACTICES/volunteer"},
        )
        resume_docs = vectorstore.similarity_search(
            question,
            k=max(top_k * 2, 12),
            filter={"category": "resume"},
        )
        volunteer_file_docs = [
            doc for doc in resume_docs
            if "volunteer" in doc.metadata.get("source", "").lower()
        ]
        return _dedupe_documents(volunteer_docs + volunteer_file_docs + resume_docs)[:top_k]

    if should_focus_profile_info(question, category_dir):
        profile_docs = vectorstore.similarity_search(
            question,
            k=4,
            filter={"source": "portfolio_app/data.py::PROFILE"},
        )
        resume_docs = vectorstore.similarity_search(
            question,
            k=max(top_k, 6),
            filter={"category": "resume"},
        )
        portfolio_docs = vectorstore.similarity_search(
            question,
            k=max(top_k, 6),
            filter={"category": "portfolio"},
        )
        return _dedupe_documents(profile_docs + resume_docs + portfolio_docs)[:top_k]

    if should_focus_research_paper_count(question, category_dir):
        direct_summary_docs = vectorstore.similarity_search(
            question,
            k=2,
            filter={"summary_kind": "research_papers_count"},
        )
        focused_docs = vectorstore.similarity_search(
            question,
            k=max(top_k * 4, 16),
            filter={"category": "papers"},
        )
        summary_docs = [
            doc for doc in focused_docs
            if doc.metadata.get("summary_kind") == "research_papers_count"
        ]
        item_docs = [
            doc for doc in focused_docs
            if doc.metadata.get("source", "").startswith("portfolio_app/data.py::RESEARCH_PAPERS/")
        ]
        return _dedupe_documents(direct_summary_docs + summary_docs + item_docs + focused_docs)[:top_k]

    if should_focus_competition_awards(question, category_dir):
        focused_docs = vectorstore.similarity_search(
            question,
            k=max(top_k * 4, 16),
            filter={"$and": [{"category": "competition"}, {"award_category": "Competition"}]},
        )
        summary_docs = [
            doc for doc in focused_docs
            if "COMPETITION_AWARDS_CATEGORY/Competition" in doc.metadata.get("source", "")
        ]
        item_docs = [
            doc for doc in focused_docs
            if doc.metadata.get("item_id")
        ]
        return _dedupe_documents(summary_docs + item_docs + focused_docs)[:top_k]

    if should_focus_sports_awards(question, category_dir):
        focused_docs = vectorstore.similarity_search(
            question,
            k=max(top_k * 4, 16),
            filter={"$and": [{"category": "competition"}, {"award_category": "Sports"}]},
        )
        summary_docs = [
            doc for doc in focused_docs
            if "COMPETITION_AWARDS_CATEGORY/Sports" in doc.metadata.get("source", "")
        ]
        item_docs = [
            doc for doc in focused_docs
            if doc.metadata.get("item_id")
        ]
        return _dedupe_documents(summary_docs + item_docs + focused_docs)[:top_k]

    where = {"category": category_dir} if category_dir else None
    return vectorstore.similarity_search(question, k=top_k, filter=where)


@st.cache_data(ttl=300, show_spinner=False)
def get_vectorstore_status() -> Dict[str, object]:
    if not CHROMA_DIR.exists():
        return {"ready": False, "chunks": 0, "updated": "Not built"}
    sqlite_file = CHROMA_DIR / "chroma.sqlite3"
    if not sqlite_file.exists():
        return {"ready": False, "chunks": 0, "updated": "Not built"}
    try:
        updated = sqlite_file.stat().st_mtime
        from datetime import datetime
        updated_text = datetime.fromtimestamp(updated).strftime("%Y-%m-%d %H:%M")
        return {"ready": True, "chunks": "Indexed", "updated": updated_text}
    except Exception:
        return {"ready": True, "chunks": "Indexed", "updated": "Unknown"}


def detect_response_language(text: str) -> str:
    normalized = text.strip().lower()
    chinese_chars = sum(1 for char in normalized if "\u4e00" <= char <= "\u9fff")
    if chinese_chars == 0:
        return "English"

    chinese_question_markers = [
        "吗", "呢", "什么", "哪里", "哪", "为什么", "怎么", "如何", "几", "多少",
        "是否", "能否", "请", "帮我", "介绍", "总结", "来自", "数据集", "文章",
        "论文", "项目", "经历", "奖项", "比赛", "？", "，", "。", "：",
    ]
    if any(marker in normalized for marker in chinese_question_markers):
        return "Chinese"

    latin_chars = sum(1 for char in normalized if "a" <= char <= "z")
    if chinese_chars >= 2 and chinese_chars >= latin_chars * 0.08:
        return "Chinese"
    return "English"


def get_no_evidence_reply(language: str) -> str:
    if language == "Chinese":
        return "\u5f53\u524d\u5206\u7c7b\u8d44\u6599\u672a\u8bb0\u5f55\u8be5\u5185\u5bb9\uff0c\u8bf7\u5207\u6362\u5176\u4ed6\u4f5c\u54c1\u96c6\u5206\u7c7b\u6216\u67e5\u770b\u5168\u90e8\u8d44\u6599\u3002"
    return "The current portfolio section does not record this information. Please switch to the Home / AI Assistant page."


def get_thinking_message(language: str, stage: str = "thinking") -> str:
    if language == "Chinese":
        messages = {
            "retrieving": "\u6b63\u5728\u68c0\u7d22\u672c\u5730\u4f5c\u54c1\u96c6\u8d44\u6599",
            "web": "正在联网检索学校与项目资料",
            "organizing": "\u6b63\u5728\u6574\u7406\u68c0\u7d22\u5230\u7684\u8bc1\u636e\u7247\u6bb5",
            "thinking": "\u6b63\u5728\u601d\u8003\u5e76\u751f\u6210\u56de\u7b54",
        }
    else:
        messages = {
            "retrieving": "Retrieving local portfolio evidence",
            "web": "Searching the web for school and program evidence",
            "organizing": "Organizing retrieved evidence chunks",
            "thinking": "Thinking and generating the answer",
        }
    return messages.get(stage, messages["thinking"])


def render_thinking_state(placeholder, language: str, stage: str = "thinking") -> None:
    placeholder.markdown(
        f"""
        <div class="thinking-card">
            <span>{get_thinking_message(language, stage)}</span>
            <span class="thinking-dots"><span></span><span></span><span></span></span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def build_messages(
        question: str,
        category_label: str,
        context: str,
        web_context: str = "",
) -> List[Dict[str, str]]:
    response_language = detect_response_language(question)
    no_evidence_reply = get_no_evidence_reply(response_language)
    current = get_current_date_context()
    history = st.session_state.get("messages", [])[-8:]
    history_text = "\n".join(
        f"{'User' if item['role'] == 'user' else 'Assistant'}: {item['content']}"
        for item in history
    )
    user_prompt = f"""Current retrieval section: {category_label}

Retrieved document chunks:
{context if context else "None"}

Web search evidence:
{web_context if web_context else "None"}

Recent conversation history:
{history_text if history_text else "None"}

User question:
{question}

Required response language: {response_language}
Current date: {current['iso']}
Current weekday: {current['weekday_en']} / {current['weekday_zh']}
Current year: {current['year']}
No-evidence sentence: {no_evidence_reply}

Language rule: You must write the answer body in the Required response language above. Do not switch language because the retrieved chunks, titles, or prior messages are in another language.

Large-model interpretation rule: If the question asks about large-model work, foundation models, generative AI, multimodal AI, or large-model engineer fit, treat retrieved evidence about Diffusion Models, Latent Diffusion, LoRA, Mamba, Transformer-based methods, medical image generation, and multimodal/vision modeling as relevant large-model/foundation-model experience. Do not reduce "large-model experience" only to LLM API products, SFT/RLHF, distributed pretraining, or inference serving. When useful, distinguish the applicant's strong generative/vision foundation-model research and LLM application engineering evidence from any missing large-scale LLM pretraining, RLHF/SFT, compression, or vLLM/Triton deployment evidence.

Evidence rule: Use Retrieved document chunks for the portfolio owner's background, achievements, papers, projects, internships, skills, and personal fit. You may use the Current date/weekday/year above for date arithmetic such as calculating age from a retrieved date of birth. Use Web search evidence only for external school/program/admission/faculty/curriculum facts. If both evidence blocks are provided, synthesize them while keeping the source boundary clear. If Retrieved document chunks is None and Web search evidence is provided, discuss only external school/program facts and say that portfolio evidence is not available. If both evidence blocks are None, reply only with the no-evidence sentence above.

Strictly follow the system rules. Answer directly from the evidence blocks in the required response language."""
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]


def stream_deepseek_answer(
        api_key: str,
        question: str,
        category_label: str,
        category_dir: Optional[str],
        top_k: int,
        placeholder,
        status_box=None,
) -> str:
    response_language = detect_response_language(question)
    render_thinking_state(placeholder, response_language, "retrieving")
    if status_box:
        status_box.update(label=get_thinking_message(response_language, "retrieving"), state="running", expanded=True)
        status_box.write(get_thinking_message(response_language, "retrieving"))
    time.sleep(0.15)

    direct_profile_answer = get_direct_profile_answer(question, response_language)
    if category_dir is None and direct_profile_answer:
        placeholder.markdown(direct_profile_answer)
        if status_box:
            status_box.update(label="Answer generated" if response_language == "English" else "回答已生成",
                              state="complete", expanded=False)
        return direct_profile_answer

    docs = retrieve_context(question, category_dir, top_k)
    render_thinking_state(placeholder, response_language, "organizing")
    if status_box:
        status_box.update(label=get_thinking_message(response_language, "organizing"), state="running", expanded=True)
        status_box.write(get_thinking_message(response_language, "organizing"))
    time.sleep(0.15)
    context = format_docs(docs)
    web_bundle: Optional[Dict[str, object]] = None
    web_context = ""
    use_web_search = should_use_web_search(question)
    if use_web_search:
        render_thinking_state(placeholder, response_language, "web")
        if status_box:
            status_box.update(label=get_thinking_message(response_language, "web"), state="running", expanded=True)
            status_box.write(get_thinking_message(response_language, "web"))
        web_bundle = search_web(question)
        web_context = format_web_context(web_bundle)
        if status_box:
            query = str(web_bundle.get("query") or "").strip() if web_bundle else ""
            error = str(web_bundle.get("error") or "").strip() if web_bundle else ""
            if query:
                status_box.write(
                    f"Search query: {query}"
                    if response_language != "Chinese"
                    else f"检索词：{query}"
                )
            if error:
                status_box.write(
                    f"Web search unavailable: {error}"
                    if response_language != "Chinese"
                    else f"联网检索暂不可用：{error}"
                )

    if not context and not web_context:
        answer = get_no_evidence_reply(response_language)
        placeholder.markdown(answer)
        if status_box:
            status_box.update(
                label="No matching evidence found" if response_language == "English" else "未检索到匹配资料",
                state="complete", expanded=False)
        return answer

    if should_focus_research_paper_count(question, category_dir) and any(
        doc.metadata.get("summary_kind") == "research_papers_count" for doc in docs
    ):
        answer = format_research_paper_count_answer(response_language)
        placeholder.markdown(answer, unsafe_allow_html=True)
        if status_box:
            status_box.update(label="Answer generated" if response_language == "English" else "回答已生成",
                              state="complete", expanded=False)
        return answer

    render_thinking_state(placeholder, response_language, "thinking")
    if status_box:
        status_box.update(label=get_thinking_message(response_language, "thinking"), state="running", expanded=True)
        status_box.write(get_thinking_message(response_language, "thinking"))
    time.sleep(0.15)
    handler = StreamHandler(placeholder)
    llm = ChatOpenAI(
        api_key=api_key,
        base_url=get_setting("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
        model=get_setting("DEEPSEEK_MODEL", "deepseek-chat"),
        temperature=0.2,
        streaming=True,
        callbacks=[handler],
    )
    llm.invoke(build_messages(question, category_label, context, web_context))
    link_html = format_portfolio_links(docs, response_language, question) if should_show_portfolio_links(question, docs) else ""
    web_links_html = format_web_source_links(web_bundle, response_language) if use_web_search else ""
    answer = handler.text + link_html + web_links_html
    handler.container.markdown(answer, unsafe_allow_html=True)
    if status_box:
        status_box.update(label="Answer generated" if response_language == "English" else "回答已生成",
                          state="complete", expanded=False)
    return answer
