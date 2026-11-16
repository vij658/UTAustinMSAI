#!/usr/bin/env bash
# Rebuild the HTML pages and commit everything locally. Run after any track change.
set -e
cd "$(dirname "$0")/.."
python3 tools/build_html.py
git add -A
git commit -q -m "${1:-checkpoint}" || echo "nothing to commit"
git push -q origin main || echo "push failed (is the repo attached to the session?)"
