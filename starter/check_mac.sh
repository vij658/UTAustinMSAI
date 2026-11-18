#!/usr/bin/env bash
# Track H setup check for macOS. Read-only: it installs nothing and changes nothing.
# Usage: bash check_mac.sh            (run from anywhere)
#        bash check_mac.sh ~/code/docdesk   (also checks your DocDesk folder)

ok()   { printf "  OK       %s\n" "$1"; }
miss() { printf "  MISSING  %s\n           -> %s\n" "$1" "$2"; MISSING=$((MISSING+1)); }
warn() { printf "  CHECK    %s\n           -> %s\n" "$1" "$2"; }
MISSING=0

echo "Track H setup check (Milestone 1: Blocks 1-6)"
echo

echo "Machine"
if [ "$(uname -s)" = "Darwin" ]; then
  ok "macOS $(sw_vers -productVersion 2>/dev/null) on $(uname -m)"
else
  warn "not macOS ($(uname -s))" "the steps in START-HERE.md are written for a Mac"
fi
echo

echo "Tools"
if command -v brew >/dev/null 2>&1; then ok "Homebrew $(brew --version 2>/dev/null | head -1 | awk '{print $2}')"
else miss "Homebrew" "install from https://brew.sh, run the PATH lines it prints, open a new Terminal"; fi

PY=""
for c in python3.13 python3.12 python3.11; do
  if command -v "$c" >/dev/null 2>&1; then PY="$c"; break; fi
done
if [ -n "$PY" ]; then ok "$PY ($($PY --version 2>&1)) - use: $PY -m venv .venv"
else miss "Python 3.11 or later" "brew install python@3.12"; fi
if command -v python3 >/dev/null 2>&1; then
  v=$(python3 -c 'import sys;print("%d.%d"%sys.version_info[:2])' 2>/dev/null)
  case "$v" in 3.1[1-9]) ;; *) warn "plain python3 is $v" "fine: always create venvs with ${PY:-python3.12}, not with python3";; esac
fi

if command -v git >/dev/null 2>&1; then ok "$(git --version)"
else miss "Git" "xcode-select --install   (or: brew install git)"; fi
n=$(git config --global user.name 2>/dev/null); e=$(git config --global user.email 2>/dev/null)
if [ -n "$n" ] && [ -n "$e" ]; then ok "Git identity set (user.name and user.email)"
else miss "Git identity" "git config --global user.name \"Your Name\"; git config --global user.email \"you@example.com\""; fi

if command -v code >/dev/null 2>&1; then ok "VS Code 'code' command"
elif [ -d "/Applications/Visual Studio Code.app" ]; then warn "VS Code installed, but 'code' is not on PATH" "in VS Code: Cmd+Shift+P -> Shell Command: Install 'code' command in PATH"
else miss "VS Code" "brew install --cask visual-studio-code"; fi
echo

echo "Network"
if curl -s -o /dev/null -m 10 -w '%{http_code}' https://api.openai.com/v1/models | grep -qE '^(200|401)$'; then
  ok "api.openai.com reachable (a 401 without a key is expected)"
else
  warn "api.openai.com not reachable" "check VPN, proxy or firewall; a work laptop may block it - use your personal Mac"
fi
echo

echo "Not needed yet (arrive later in Track H)"
for t in docker ollama psql aws terraform; do
  if command -v "$t" >/dev/null 2>&1; then printf "  present  %s\n" "$t"; else printf "  later    %s\n" "$t"; fi
done
echo "           docker: Block 9, ollama: Block 6, psql: Block 10, aws: Block 14, terraform: Block 21"
echo

if [ -n "$1" ]; then
  D="${1/#\~/$HOME}"
  echo "DocDesk folder: $D"
  if [ -d "$D" ]; then
    [ -f "$D/.gitignore" ] && ok ".gitignore present" || miss ".gitignore" "copy it from the starter kit"
    if [ -f "$D/.env" ]; then
      if grep -qE '^OPENAI_API_KEY=.+' "$D/.env" && ! grep -qE '^OPENAI_API_KEY=(sk-your-key-here)?$' "$D/.env"; then
        ok ".env has an OPENAI_API_KEY value (not shown)"
      else
        warn ".env has no real OPENAI_API_KEY yet" "paste your key after OPENAI_API_KEY= (no quotes, no spaces)"
      fi
    else
      warn "no .env yet" "cp .env.example .env, then paste your key (Block 1)"
    fi
    if [ -d "$D/.git" ]; then
      if git -C "$D" ls-files --error-unmatch .env >/dev/null 2>&1; then
        miss ".env is TRACKED by Git" "git rm --cached .env && git commit -m 'stop tracking .env' - then rotate the key"
      else
        ok ".env is not tracked by Git"
      fi
    else
      warn "not a Git repository yet" "cd $D && git init"
    fi
    [ -d "$D/.venv" ] && ok ".venv present" || warn "no .venv yet" "created in Block 1: ${PY:-python3.12} -m venv .venv"
  else
    warn "folder not found" "cp -R docdesk ~/code/docdesk (START-HERE.md, Step 4)"
  fi
  echo
fi

if [ "$MISSING" -eq 0 ]; then
  echo "Ready for Block 1."
else
  echo "$MISSING item(s) missing; install them and run this again."
fi
