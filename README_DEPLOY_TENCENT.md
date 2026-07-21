# Tencent Cloud Deployment Guide

This project is a Streamlit portfolio RAG Agent. It uses local portfolio data from `docs/`, `data/`, and a Chroma vector store. For school/application questions, it can also run web search.

## Required runtime files

- `portfolio_app/` - application source code
- `data/` - portfolio images, PDFs, and structured assets
- `docs/` - RAG text/PDF documents
- `requirements.txt`
- `run_app.py`
- `.streamlit/config.toml`
- `Dockerfile`
- `docker-compose.yml`
- `scripts/`

`chroma_db/` is generated from `docs/` and `data`. It can be mounted as a persistent volume or rebuilt on first container startup.

Files and folders intentionally excluded from deployment/image build:

- `.env` - local secret file
- `.hf_cache/` - local embedding model cache; mount it as a volume on the server instead
- `.conda_env/`, `__pycache__/`, `tmp/`, logs, pid/job files
- `portfolio_source.pptx`, `pptx_extracted_text.txt`, `mdhgfn_render_dump.txt` - local source/extraction artifacts

## Environment variables

Create `.env` on the server:

```bash
DEEPSEEK_API_KEY=your_deepseek_api_key_here
WEB_SEARCH_MAX_RESULTS=5
WEB_SEARCH_MAX_PAGES=3
WEB_SEARCH_TIMEOUT=10
```

Do not commit `.env` or bake it into the Docker image.

## Deploy with Docker Compose

```bash
cd /opt/portfolio-agent
cp .env.example .env
nano .env
docker compose up --build -d
docker compose logs -f portfolio-agent
```

If you upload files manually, upload the cleaned project directory but do not upload `.env`; create `.env` directly on the Tencent Cloud server.

The first startup may take several minutes because it downloads the embedding model and rebuilds `chroma_db` if it is missing.

## Tencent Cloud checklist

- Use a Tencent Cloud CVM or Lighthouse instance with at least 2 CPU cores and 4 GB RAM. 8 GB RAM is safer for rebuilding embeddings.
- Open inbound TCP port `8501` in the Security Group if exposing Streamlit directly.
- Prefer Nginx on ports `80/443` for production, proxying to `127.0.0.1:8501`.
- Keep outbound network access enabled for DeepSeek API, web search, and the Hugging Face mirror.
- Use a persistent disk or host volume for `./chroma_db` and `./.hf_cache` to avoid rebuilding on every redeploy.

## Nginx reverse proxy example

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_read_timeout 86400;
    }
}
```

## Useful commands

Rebuild vector store manually:

```bash
docker compose exec portfolio-agent python scripts/rebuild_vectorstore.py
```

Check service health:

```bash
curl http://127.0.0.1:8501/_stcore/health
```

Restart:

```bash
docker compose restart portfolio-agent
```
