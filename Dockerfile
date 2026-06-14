# AI-KungFU East Africa MCP Server
# Glama-compatible Dockerfile for elimu-mcp
FROM python:3.12-slim

LABEL org.opencontainers.image.source="https://github.com/gabrielmahia/elimu-mcp"
LABEL org.opencontainers.image.description="elimu-mcp — East Africa AI Coordination Infrastructure"
LABEL org.opencontainers.image.licenses="MIT"

RUN pip install --no-cache-dir elimu-mcp

CMD ["elimu-mcp"]
