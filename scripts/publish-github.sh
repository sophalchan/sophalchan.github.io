#!/usr/bin/env bash
# Publish Quarto portfolio to https://sophalchan.github.io
set -euo pipefail

REPO="sophalchan.github.io"
OWNER="sophalchan"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
GH="${GH_BIN:-gh}"

cd "$ROOT"

if ! "$GH" auth status &>/dev/null; then
  echo ">>> Log in to GitHub (browser or token)..."
  "$GH" auth login --hostname github.com --git-protocol https --web --scopes repo,workflow,read:org
fi

if ! git rev-parse --git-dir &>/dev/null; then
  git init -b main
fi

if ! git rev-parse HEAD &>/dev/null 2>&1; then
  git add .
  git commit -m "$(cat <<'EOF'
Add Quarto portfolio site for GitHub Pages.

Cybersecurity, AI/ML, and data analytics project hub with CI deploy.
EOF
)"
fi

if ! "$GH" repo view "$OWNER/$REPO" &>/dev/null; then
  "$GH" repo create "$REPO" --public --description "Sophal Chan — Cybersecurity & Data Analytics Portfolio"
fi

if ! git remote get-url origin &>/dev/null; then
  git remote add origin "https://github.com/$OWNER/$REPO.git"
fi

git push -u origin main

"$GH" api "repos/$OWNER/$REPO/pages" -X PUT -f build_type=workflow 2>/dev/null || \
  "$GH" api "repos/$OWNER/$REPO/pages" -X POST -f build_type=workflow

echo ""
echo "Pushed to https://github.com/$OWNER/$REPO"
echo "GitHub Actions will build the site. Live URL (after first workflow run):"
echo "  https://$OWNER.github.io/"
