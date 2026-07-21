import os
from pathlib import Path
from typing import Dict, Optional

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parent.parent
if os.getenv("USE_HF_MIRROR") == "1":
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
os.environ.setdefault("HUGGINGFACE_HUB_CACHE", str(BASE_DIR / ".hf_cache"))
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")

DOCS_DIR = BASE_DIR / "docs"
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = BASE_DIR / "chroma_db"
COLLECTION_NAME = "portfolio_rag"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
AVATAR_PATH = DATA_DIR / "f391770cecab6e1a2f36380b066250b.jpg"
SCHOOL_ICON_PATH = DATA_DIR / "school.png"
RESEARCH_DIR = DATA_DIR / "research"
RESEARCH_THUMB_DIR = DATA_DIR / "research_thumbs"
COMPETITION_DIR = DATA_DIR / "Competition Awards"
PROJECTS_DIR = DATA_DIR / "Websites and systems"

CATEGORIES: Dict[str, Optional[str]] = {
    "Home / AI Assistant": None,
    "Research Papers": "papers",
    "Competitions & Awards": "competition",
    "Engineering Projects": "projects",
    "Internships & Practices": "resume",
    "Resume & Internship": "resume",
}

CATEGORY_LABEL_BY_DIR = {
    "papers": "Research Papers",
    "competition": "Competitions",
    "projects": "Engineering Projects",
    "resume": "Internships & Practices",
}

SUPPORTED_SUFFIXES = {".pdf", ".md", ".txt"}

PORTFOLIO_PDF = BASE_DIR / "data" / "陈梓深作品集.pdf"

WEB_SEARCH_MAX_RESULTS = int(os.getenv("WEB_SEARCH_MAX_RESULTS", "5"))
WEB_SEARCH_MAX_PAGES = int(os.getenv("WEB_SEARCH_MAX_PAGES", "3"))
WEB_SEARCH_TIMEOUT = int(os.getenv("WEB_SEARCH_TIMEOUT", "10"))


def get_setting(name: str, default: str = "") -> str:
    value = os.getenv(name)
    if value:
        return value
    try:
        import streamlit as st

        secret_value = st.secrets.get(name)
    except Exception:
        return default
    if secret_value is None:
        return default
    return str(secret_value)
