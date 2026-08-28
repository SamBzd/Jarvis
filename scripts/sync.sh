#!/usr/bin/env bash

set -u

usage() {
  cat <<'EOF'
Usage: scripts/sync.sh [--repo-root PATH]

Met à jour le dépôt Jarvis avec git pull --ff-only.
Ne fusionne, ne rebase, ne stash et ne restaure jamais automatiquement.

Codes utiles :
  10 dépôt sale
  11 remote origin absent
  12 upstream absent
  13 pull impossible ou divergence
  14 branche différente de main
EOF
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd "${script_dir}/.." && pwd -P)"

while (($#)); do
  case "$1" in
    --repo-root)
      if (($# < 2)); then
        echo "Erreur : --repo-root attend un chemin." >&2
        exit 64
      fi
      repo_root="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Erreur : argument inconnu : $1" >&2
      usage >&2
      exit 64
      ;;
  esac
done

if ! git -C "${repo_root}" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Synchronisation ignorée : ${repo_root} n'est pas un dépôt Git." >&2
  exit 2
fi

branch="$(git -C "${repo_root}" branch --show-current)"
if [[ "${branch}" != "main" ]]; then
  echo "Synchronisation refusée : branche courante '${branch:-détachée}', main attendue." >&2
  exit 14
fi

if [[ -n "$(git -C "${repo_root}" status --porcelain=v1 --untracked-files=all)" ]]; then
  echo "Synchronisation refusée : le dépôt Jarvis contient des changements locaux." >&2
  exit 10
fi

if ! git -C "${repo_root}" remote get-url origin >/dev/null 2>&1; then
  echo "Synchronisation ignorée : aucun remote origin n'est configuré." >&2
  exit 11
fi

if ! upstream="$(git -C "${repo_root}" rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null)"; then
  echo "Synchronisation ignorée : la branche main n'a pas d'upstream." >&2
  exit 12
fi
if [[ "${upstream}" != "origin/main" ]]; then
  echo "Synchronisation refusée : upstream '${upstream}', origin/main attendu." >&2
  exit 12
fi

if ! git -C "${repo_root}" pull --ff-only; then
  echo "Synchronisation impossible sans résolution manuelle. Aucun merge ou rebase automatique n'a été lancé." >&2
  exit 13
fi

echo "Mémoire Jarvis synchronisée. Un AGENTS.md modifié s'appliquera à la prochaine session Codex."
