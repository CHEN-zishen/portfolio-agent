# Deploy To Streamlit Community Cloud

This app is ready for Streamlit Community Cloud.

## Required Files

- `run_app.py` is the app entry point.
- `requirements.txt` contains Python dependencies.
- `packages.txt` contains Linux system packages.
- `runtime.txt` pins Python 3.10.
- `.streamlit/secrets.toml.example` shows the required secrets format.

## Deploy Steps

1. Push this project to a GitHub repository.
2. Open Streamlit Community Cloud and create a new app from that repository.
3. Set the main file path to `run_app.py`.
4. Add this secret in the app settings:

```toml
DEEPSEEK_API_KEY = "your_deepseek_api_key_here"
```

Optional secrets:

```toml
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"
WEB_SEARCH_MAX_RESULTS = "5"
WEB_SEARCH_MAX_PAGES = "3"
WEB_SEARCH_TIMEOUT = "10"
```

The app will build `chroma_db` automatically on first startup if the vector store is missing.
For cloud deployments, leave `USE_HF_MIRROR` unset or set it to `0`.
