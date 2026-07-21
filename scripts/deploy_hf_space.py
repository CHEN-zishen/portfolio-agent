import argparse
import os
from pathlib import Path

import requests
from dotenv import dotenv_values
from huggingface_hub import HfApi, configure_http_backend, create_repo


ROOT = Path(__file__).resolve().parent.parent


def _no_proxy_session() -> requests.Session:
    session = requests.Session()
    session.trust_env = False
    proxy = os.getenv("HF_DEPLOY_PROXY")
    if proxy:
        session.proxies.update({"http": proxy, "https": proxy})
    return session


configure_http_backend(backend_factory=_no_proxy_session)


IGNORE_PATTERNS = [
    ".env",
    ".env.local",
    ".env.production",
    ".streamlit/secrets.toml",
    ".git/*",
    ".agents/*",
    ".hf_cache/*",
    ".conda_env/*",
    "chroma_db/*",
    "dist/*",
    "tmp/*",
    "work/*",
    "outputs/*",
    "__pycache__/*",
    "**/__pycache__/*",
    "*.pyc",
    "*.pyo",
    "*.pyd",
    ".pytest_cache/*",
    ".mypy_cache/*",
    ".ruff_cache/*",
    "*.log",
    "*.pid",
    "*.jobid",
    "*.out",
    "*.err",
    "*.out.log",
    "*.err.log",
    "portfolio_source.pptx",
    "pptx_extracted_text.txt",
    "mdhgfn_render_dump.txt",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Deploy this Streamlit app to Hugging Face Spaces.")
    parser.add_argument("--repo-id", required=True, help="Space repo id, for example username/portfolio-agent")
    parser.add_argument("--token", default=os.getenv("HF_TOKEN"), help="Hugging Face token, or set HF_TOKEN")
    parser.add_argument("--private", action="store_true", help="Create the Space as private")
    args = parser.parse_args()

    if not args.token:
        raise SystemExit("Missing Hugging Face token. Pass --token or set HF_TOKEN.")

    create_repo(
        repo_id=args.repo_id,
        repo_type="space",
        space_sdk="docker",
        private=args.private,
        token=args.token,
        exist_ok=True,
    )

    api = HfApi(token=args.token)
    api.upload_folder(
        folder_path=str(ROOT),
        repo_id=args.repo_id,
        repo_type="space",
        path_in_repo=".",
        ignore_patterns=IGNORE_PATTERNS,
        commit_message="Deploy portfolio agent",
    )

    local_env = dotenv_values(ROOT / ".env")
    deepseek_key = local_env.get("DEEPSEEK_API_KEY")
    if deepseek_key:
        api.add_space_secret(args.repo_id, "DEEPSEEK_API_KEY", deepseek_key)

    for name, default_value in {
        "WEB_SEARCH_MAX_RESULTS": "5",
        "WEB_SEARCH_MAX_PAGES": "3",
        "WEB_SEARCH_TIMEOUT": "10",
    }.items():
        api.add_space_variable(args.repo_id, name, local_env.get(name) or default_value)

    print(f"Deployed: https://huggingface.co/spaces/{args.repo_id}")


if __name__ == "__main__":
    main()
