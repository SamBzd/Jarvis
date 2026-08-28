#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: scripts/install.sh [--dry-run] [--codex-home PATH]

Crée le lien AGENTS.md global sans modifier config.toml.
--codex-home est surtout utile pour les tests ou une installation non standard.
EOF
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd "${script_dir}/.." && pwd -P)"
codex_home_arg=""
dry_run=false

while (($#)); do
  case "$1" in
    --dry-run)
      dry_run=true
      shift
      ;;
    --codex-home)
      if (($# < 2)); then
        echo "Erreur : --codex-home attend un chemin." >&2
        exit 64
      fi
      codex_home_arg="$2"
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

if [[ -n "${codex_home_arg}" ]]; then
  codex_home="${codex_home_arg}"
elif [[ -n "${CODEX_HOME:-}" ]]; then
  codex_home="${CODEX_HOME}"
else
  codex_home="${HOME:?HOME doit être défini}/.codex"
fi

source_agents="${repo_root}/AGENTS.md"
target_agents="${codex_home}/AGENTS.md"
override_agents="${codex_home}/AGENTS.override.md"

if [[ ! -s "${source_agents}" ]]; then
  echo "Erreur : contrat Jarvis absent ou vide : ${source_agents}" >&2
  exit 2
fi

if [[ -e "${override_agents}" || -L "${override_agents}" ]]; then
  echo "Erreur : ${override_agents} existe et peut masquer AGENTS.md." >&2
  echo "Examine-le manuellement avant d'installer Jarvis." >&2
  exit 3
fi

if [[ -L "${target_agents}" ]]; then
  current_target="$(readlink -f "${target_agents}" 2>/dev/null || true)"
  expected_target="$(readlink -f "${source_agents}")"
  if [[ "${current_target}" == "${expected_target}" ]]; then
    echo "Jarvis est déjà relié à ${target_agents}."
    exit 0
  fi
  echo "Erreur : ${target_agents} est déjà un lien vers une autre cible." >&2
  exit 4
fi

if [[ -e "${target_agents}" ]]; then
  echo "Erreur : ${target_agents} existe déjà. Aucun fichier ne sera écrasé." >&2
  exit 4
fi

if [[ "${dry_run}" == true ]]; then
  echo "Simulation : création de ${target_agents} -> ${source_agents}"
  echo "La configuration Codex reste inchangée."
  exit 0
fi

mkdir -p "${codex_home}"
ln -s "${source_agents}" "${target_agents}"

linked_target="$(readlink -f "${target_agents}")"
expected_target="$(readlink -f "${source_agents}")"
if [[ "${linked_target}" != "${expected_target}" ]]; then
  echo "Erreur : le lien créé ne pointe pas vers le contrat attendu." >&2
  exit 5
fi

echo "Jarvis est relié à ${target_agents}."
echo "Ajoute manuellement config/config.toml.example à ta configuration si nécessaire."
echo "Ouvre une nouvelle session Codex pour charger le contrat."
