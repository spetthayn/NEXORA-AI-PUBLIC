#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
cat part-*.b64 | base64 -d > nexora-ai-src.tar.gz
echo "SHA256:"
(sha256sum nexora-ai-src.tar.gz 2>/dev/null || shasum -a 256 nexora-ai-src.tar.gz)
tar xzf nexora-ai-src.tar.gz
echo "Extracted ./nexora-ai"
ls nexora-ai | head
