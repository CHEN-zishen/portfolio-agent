#!/usr/bin/env bash
set -euo pipefail

if [ ! -f "/app/chroma_db/chroma.sqlite3" ]; then
  echo "Chroma vector store not found. Rebuilding from /app/docs and /app/data..."
  python /app/scripts/rebuild_vectorstore.py
fi

exec streamlit run /app/run_app.py \
  --server.address=0.0.0.0 \
  --server.port="${PORT:-8501}" \
  --server.headless=true
