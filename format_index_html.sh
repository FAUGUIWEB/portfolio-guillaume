#!/usr/bin/env bash
set -euo pipefail

# Format HTML only. Strict whitespace sensitivity prevents formatter-added
# spaces/newlines from changing inline typography (notably NEW DROP spans).
npx --yes prettier@3.6.2 index.html \
  --write \
  --parser html \
  --print-width 110 \
  --tab-width 2 \
  --html-whitespace-sensitivity strict
