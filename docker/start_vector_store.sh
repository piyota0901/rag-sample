#!/bin/bash
# qdrant-localという名前のコンテナが存在する場合は削除、存在しない場合は何もしない
docker rm -f qdrant-local || true
docker run -d --name qdrant-local -p 6333:6333 qdrant/qdrant
poetry run python ./setup_db.py