from pathlib import Path
from typing import Dict

import streamlit as st

from .config import AVATAR_PATH, PORTFOLIO_PDF, RESEARCH_THUMB_DIR

@st.cache_data(show_spinner=False)
def get_avatar_base64() -> str:
    try:
        if AVATAR_PATH.exists():
            if AVATAR_PATH.stat().st_size > 5 * 1024 * 1024:
                return ""
            import base64
            with open(AVATAR_PATH, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
    except Exception:
        pass
    return ""


@st.cache_data(show_spinner=False)
def get_image_base64(path: Path) -> str:
    if not path.exists():
        return ""
    import base64
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


@st.cache_data(show_spinner=False)
def read_file_bytes(path: Path) -> bytes:
    if not path.exists():
        return b""
    return path.read_bytes()


def _cache_stem(path: Path, limit: int = 56) -> str:
    import hashlib

    raw = str(path.resolve() if path.exists() else path).lower()
    digest = hashlib.md5(raw.encode("utf-8")).hexdigest()[:10]
    safe = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in path.stem)
    safe = safe[:limit].strip("_") or "asset"
    return f"{safe}_{digest}"


@st.cache_resource(show_spinner=False)
def get_pdf_doc(pdf_path: Path):
    """Cache PDF document object to avoid repeated opening."""
    try:
        import fitz
        if pdf_path.exists():
            return fitz.open(pdf_path)
    except Exception:
        pass
    return None


@st.cache_data(show_spinner=False)
def get_pdf_thumbnail(pdf_path: Path) -> str:
    """Render the first PDF page to a cached PNG thumbnail (high res 2x)."""
    if not pdf_path.exists():
        return ""
    try:
        import fitz
    except Exception:
        return ""

    RESEARCH_THUMB_DIR.mkdir(parents=True, exist_ok=True)
    thumb_path = RESEARCH_THUMB_DIR / f"{_cache_stem(pdf_path, 62)}_hi.png"
    if thumb_path.exists():
        return get_image_base64(thumb_path)
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)
        pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), alpha=False)
        pix.save(thumb_path)
        doc.close()
        return get_image_base64(thumb_path)
    except Exception:
        return ""


def _clear_connected_white_background(image, threshold: int = 248) -> None:
    """Make only edge-connected white page background transparent."""
    from collections import deque

    pixels = image.load()
    width, height = image.size
    if width == 0 or height == 0:
        return

    visited = set()
    queue = deque()

    def is_background(x: int, y: int) -> bool:
        r, g, b, a = pixels[x, y]
        return a == 0 or (a > 0 and r >= threshold and g >= threshold and b >= threshold)

    def push(x: int, y: int) -> None:
        if x < 0 or y < 0 or x >= width or y >= height:
            return
        key = (x, y)
        if key in visited or not is_background(x, y):
            return
        visited.add(key)
        queue.append(key)

    for x in range(width):
        push(x, 0)
        push(x, height - 1)
    for y in range(height):
        push(0, y)
        push(width - 1, y)

    while queue:
        x, y = queue.popleft()
        r, g, b, a = pixels[x, y]
        if a:
            pixels[x, y] = (r, g, b, 0)
        push(x - 1, y)
        push(x + 1, y)
        push(x, y - 1)
        push(x, y + 1)


def _redact_review_artifacts(page) -> None:
    """Remove manuscript page furniture before rendering cropped figure thumbnails."""
    try:
        import fitz
    except Exception:
        return

    try:
        blocks = page.get_text("blocks")
    except Exception:
        return

    page_rect = page.rect
    added = False

    def add(rect) -> None:
        nonlocal added
        rect = fitz.Rect(rect)
        rect.x0 = max(0, rect.x0)
        rect.y0 = max(0, rect.y0)
        rect.x1 = min(page_rect.width, rect.x1)
        rect.y1 = min(page_rect.height, rect.y1)
        if rect.width <= 0 or rect.height <= 0:
            return
        page.add_redact_annot(rect, fill=None, cross_out=False)
        added = True

    for block in blocks:
        if len(block) < 5:
            continue
        block_type = block[6] if len(block) > 6 else 0
        if block_type != 0:
            continue
        x0, y0, x1, y1, text = block[:5]
        text = " ".join(str(text).split())
        if not text:
            continue

        rect = fitz.Rect(x0 - 1, y0 - 1, x1 + 1, y1 + 1)
        if text.startswith("Page ") and (y0 < 35 or x0 < 35 or x1 > page_rect.width - 90):
            if y0 < 35:
                rect.y0 = 0
            add(rect)
        else:
            parts = text.split()
            is_line_numbers = len(parts) >= 8 and all(part.isdigit() for part in parts[:8])
            if is_line_numbers and x1 < 35:
                add((0, max(0, y0 - 1), min(page_rect.width, x1 + 1), min(page_rect.height, y1 + 1)))

    if not added:
        return
    try:
        page.apply_redactions(
            images=fitz.PDF_REDACT_IMAGE_NONE,
            graphics=fitz.PDF_REDACT_LINE_ART_NONE,
            text=fitz.PDF_REDACT_TEXT_REMOVE,
        )
    except TypeError:
        page.apply_redactions()


@st.cache_data(show_spinner=False)
def get_pdf_clean_thumbnail(pdf_path: Path, zoom: float = 2.7) -> str:
    """Render a PDF artwork/table with transparent page background and tight bounds."""
    if not pdf_path.exists():
        return ""
    try:
        import fitz
    except Exception:
        return ""

    RESEARCH_THUMB_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = _cache_stem(pdf_path, 62)
    thumb_path = RESEARCH_THUMB_DIR / f"{safe_name}_clean_{int(zoom * 10)}_v5.png"
    if thumb_path.exists():
        return get_image_base64(thumb_path)

    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)
        _redact_review_artifacts(page)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True)
        doc.close()

        try:
            from PIL import Image

            mode = "RGBA" if pix.alpha else "RGB"
            image = Image.frombytes(mode, (pix.width, pix.height), pix.samples)
            if image.mode != "RGBA":
                image = image.convert("RGBA")
            _clear_connected_white_background(image)

            bbox = image.getbbox()
            if bbox:
                pad = max(2, int(zoom))
                left = max(0, bbox[0] - pad)
                top = max(0, bbox[1] - pad)
                right = min(image.width, bbox[2] + pad)
                bottom = min(image.height, bbox[3] + pad)
                image = image.crop((left, top, right, bottom))
            image.save(thumb_path)
        except Exception:
            pix.save(thumb_path)

        return get_image_base64(thumb_path)
    except Exception:
        return ""


@st.cache_data(show_spinner=False)
def get_pdf_svg(pdf_path: Path, page_index: int = 0) -> str:
    """Render a PDF page to a clean SVG vector markup (lossless, crisp at any zoom)."""
    if not pdf_path.exists():
        return ""
    try:
        import fitz
    except Exception:
        return ""
    try:
        doc = fitz.open(pdf_path)
        if page_index >= len(doc):
            doc.close()
            return ""
        page = doc.load_page(page_index)
        svg = page.get_svg_image(matrix=fitz.Identity, text_as_path=False)
        doc.close()
        if svg:
            svg = svg.replace("<?xml version=\"1.0\" encoding=\"UTF-8\"?>", "").strip()
            svg = svg.replace(" width=\"", ' preserveAspectRatio="xMidYMid meet" width="')
            return svg
        return ""
    except Exception:
        return ""


@st.cache_data(show_spinner=False)
def get_pdf_page_image(pdf_path: Path, page_index: int, zoom: float = 1.0) -> str:
    """Render a selected PDF page to a cached PNG for paper detail pages."""
    if not pdf_path.exists():
        return ""
    try:
        import fitz
    except Exception:
        return ""

    RESEARCH_THUMB_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = _cache_stem(pdf_path, 54)
    page_path = RESEARCH_THUMB_DIR / f"{safe_name}_page_{page_index + 1}.png"
    if page_path.exists():
        return get_image_base64(page_path)
    try:
        doc = fitz.open(pdf_path)
        if page_index >= len(doc):
            doc.close()
            return ""
        page = doc.load_page(page_index)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        pix.save(page_path)
        doc.close()
        return get_image_base64(page_path)
    except Exception:
        return ""


@st.cache_data(show_spinner=False)
def get_portfolio_image(page_index: int, zoom: float = 1.0) -> str:
    """Render a page from the portfolio PDF."""
    if not PORTFOLIO_PDF.exists():
        return ""
    try:
        import fitz
    except Exception:
        return ""

    RESEARCH_THUMB_DIR.mkdir(parents=True, exist_ok=True)
    page_path = RESEARCH_THUMB_DIR / f"portfolio_page_{page_index + 1}.png"
    if page_path.exists():
        return get_image_base64(page_path)
    try:
        doc = fitz.open(PORTFOLIO_PDF)
        if page_index >= len(doc):
            doc.close()
            return ""
        page = doc.load_page(page_index)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        pix.save(page_path)
        doc.close()
        return get_image_base64(page_path)
    except Exception:
        return ""


def get_research_visual(paper: Dict) -> str:
    """Return a visual block using explicit cover image, or portfolio PDF image, or fallback."""
    cover = paper.get("cover")
    if cover:
        b64 = get_image_base64(cover)
        if b64:
            return f'<img class="paper-image" src="data:image/png;base64,{b64}" />'
    portfolio_pages = paper.get("portfolio_pages", [])
    if portfolio_pages:
        image_base64 = get_portfolio_image(portfolio_pages[0], zoom=0.8)
        if image_base64:
            return f'<img class="paper-image" src="data:image/png;base64,{image_base64}" />'
    initials = "".join(word[0] for word in paper["tag"].split()[:2]).upper()
    return (
        '<div class="paper-image paper-fallback">'
        f'<div class="paper-fallback-mark">{initials}</div>'
        f'<div class="paper-fallback-topic">{paper["tag"]}</div>'
        '</div>'
    )
