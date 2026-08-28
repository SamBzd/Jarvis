#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd "${script_dir}/.." && pwd -P)"

required_files=(
  "README.md"
  "AGENTS.md"
  "config/config.toml.example"
  "memory/README.md"
  "memory/profile.md"
  "memory/projects.md"
  "memory/recent-sessions.md"
  "standards/design-decisions.md"
  "standards/project-conventions.md"
  "standards/capabilities.md"
  "scripts/install.sh"
  "scripts/sync.sh"
  "scripts/close-session.py"
  "tests/test_scripts.py"
  "tests/manual-scenarios.md"
)

for relative_path in "${required_files[@]}"; do
  if [[ ! -s "${repo_root}/${relative_path}" ]]; then
    echo "Fichier requis absent ou vide : ${relative_path}" >&2
    exit 1
  fi
done

agents_size="$(wc -c < "${repo_root}/AGENTS.md")"
if ((agents_size >= 32768)); then
  echo "AGENTS.md dépasse la cible de 32 Kio : ${agents_size} octets." >&2
  exit 1
fi

bash -n "${repo_root}/scripts/install.sh"
bash -n "${repo_root}/scripts/sync.sh"
bash -n "${repo_root}/scripts/check.sh"

python3 -c 'import pathlib, sys; compile(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"), sys.argv[1], "exec")' "${repo_root}/scripts/close-session.py"
python3 -c 'import pathlib, sys; compile(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"), sys.argv[1], "exec")' "${repo_root}/tests/test_scripts.py"

if command -v rg >/dev/null 2>&1; then
  if rg -n --hidden \
    --glob '!scripts/close-session.py' \
    --glob '!tests/test_scripts.py' \
    '(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----)' \
    "${repo_root}"; then
    echo "Une chaîne ressemblant à un secret a été détectée." >&2
    exit 1
  fi
fi

python3 "${repo_root}/tests/test_scripts.py"

echo "Validation Jarvis réussie (${agents_size} octets pour AGENTS.md)."
