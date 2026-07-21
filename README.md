# Zishen Chen Portfolio Agent

Interactive Streamlit portfolio and RAG assistant for Zishen Chen.

## Streamlit Community Cloud

Deploy from GitHub with:

- Main file path: `run_app.py`
- Python dependencies: `requirements.txt`
- System packages: `packages.txt`
- Python runtime: `runtime.txt`

## Secrets

Set this in Streamlit Cloud `Advanced settings -> Secrets`:

```toml
DEEPSEEK_API_KEY = "your_deepseek_api_key_here"
```

Optional settings:

```toml
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"
WEB_SEARCH_MAX_RESULTS = "5"
WEB_SEARCH_MAX_PAGES = "3"
WEB_SEARCH_TIMEOUT = "10"
```

The app uses local portfolio data from `docs/`, `data/`, and structured entries in `portfolio_app/data.py`.
If `chroma_db` is missing, it builds the searchable knowledge base on startup.
