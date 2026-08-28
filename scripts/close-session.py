#!/usr/bin/env python3
"""Clôture contrôlée d'une session Jarvis.

Le script accepte un résumé JSON, met à jour uniquement la FIFO et, pour un
projet connu, sa date de dernière session. Il refuse tout dépôt non propre,
toute divergence et tout fichier modifié hors de ce périmètre.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Iterable


ALLOWED_SCOPES = {"general", "project"}
CONTENT_FIELDS = ("context", "completed", "decisions", "state", "next")
REQUIRED_FIELDS = {"date", "scope", "title", *CONTENT_FIELDS}
OPTIONAL_FIELDS = {"project_id"}
MIN_WORDS = 80
MAX_WORDS = 120
MAX_FIELD_CHARS = 700
MAX_TITLE_CHARS = 120
SESSION_START = "<!-- sessions:start -->"
SESSION_END = "<!-- sessions:end -->"
ALLOWED_MEMORY_FILES = {
    "memory/recent-sessions.md",
    "memory/projects.md",
}

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", re.I),
    re.compile(r"\b(?:ghp|github_pat|sk|xox[baprs])_[A-Za-z0-9_-]{12,}\b"),
    re.compile(r"\b(?:api[_ -]?key|password|passwd|secret|access[_ -]?token)\s*[:=]\s*\S+", re.I),
    re.compile(r"https?://[^\s/:]+:[^\s/@]+@", re.I),
)


class ClosureError(RuntimeError):
    """Erreur attendue qui doit être présentée sans traceback."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clôture contrôlée d'une session Jarvis")
    parser.add_argument("--input", required=True, type=Path, help="Résumé JSON préparé pour la clôture")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Racine du dépôt Jarvis (tests uniquement en usage normal)",
    )
    return parser.parse_args()


def run_git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or "commande Git en échec"
        raise ClosureError(f"Git {' '.join(args)} : {detail}")
    return result


def word_count(values: Iterable[str]) -> int:
    text = " ".join(values)
    return len(re.findall(r"[\wÀ-ÖØ-öø-ÿ]+(?:['’-][\wÀ-ÖØ-öø-ÿ]+)*", text, flags=re.UNICODE))


def validate_no_secret(text: str) -> None:
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise ClosureError("Le résumé ressemble à une donnée secrète ou à une URL authentifiée.")


def load_payload(path: Path) -> dict[str, str]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ClosureError(f"Résumé illisible : {exc}") from exc

    validate_no_secret(raw)
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ClosureError(f"JSON invalide : {exc}") from exc

    if not isinstance(payload, dict):
        raise ClosureError("Le résumé JSON doit être un objet.")

    keys = set(payload)
    missing = REQUIRED_FIELDS - keys
    extra = keys - REQUIRED_FIELDS - OPTIONAL_FIELDS
    if missing:
        raise ClosureError(f"Champs manquants : {', '.join(sorted(missing))}.")
    if extra:
        raise ClosureError(f"Champs non autorisés : {', '.join(sorted(extra))}.")

    for key, value in payload.items():
        if not isinstance(value, str):
            raise ClosureError(f"Le champ {key} doit être une chaîne.")
        payload[key] = value.strip()

    for field in REQUIRED_FIELDS:
        if not payload[field]:
            raise ClosureError(f"Le champ {field} est vide.")

    try:
        dt.date.fromisoformat(payload["date"])
    except ValueError as exc:
        raise ClosureError("La date doit respecter AAAA-MM-JJ.") from exc

    if payload["scope"] not in ALLOWED_SCOPES:
        raise ClosureError("La portée doit être 'general' ou 'project'.")

    if len(payload["title"]) > MAX_TITLE_CHARS:
        raise ClosureError(f"Le titre dépasse {MAX_TITLE_CHARS} caractères.")

    for field in CONTENT_FIELDS:
        if len(payload[field]) > MAX_FIELD_CHARS:
            raise ClosureError(f"Le champ {field} dépasse {MAX_FIELD_CHARS} caractères.")

    project_id = payload.get("project_id", "")
    if payload["scope"] == "project":
        if not project_id:
            raise ClosureError("project_id est obligatoire pour une session projet.")
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", project_id):
            raise ClosureError("project_id contient des caractères non autorisés.")
    elif project_id:
        raise ClosureError("project_id est interdit pour une session générale.")

    count = word_count(payload[field] for field in ("title", *CONTENT_FIELDS))
    if not MIN_WORDS <= count <= MAX_WORDS:
        raise ClosureError(f"Le résumé contient {count} mots ; {MIN_WORDS} à {MAX_WORDS} sont requis.")

    validate_no_secret("\n".join(payload.values()))
    return payload


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def render_entry(payload: dict[str, str]) -> str:
    scope_label = payload.get("project_id") or "général"
    return "\n".join(
        (
            f"## {payload['date']} — {scope_label} — {payload['title']}",
            "",
            f"- Contexte : {payload['context']}",
            f"- Réalisé : {payload['completed']}",
            f"- Décisions : {payload['decisions']}",
            f"- État : {payload['state']}",
            f"- Prochaine action : {payload['next']}",
        )
    )


def update_sessions(original: str, payload: dict[str, str]) -> str:
    if original.count(SESSION_START) != 1 or original.count(SESSION_END) != 1:
        raise ClosureError("Les marqueurs FIFO sont absents ou ambigus.")

    before, remainder = original.split(SESSION_START, 1)
    current, after = remainder.split(SESSION_END, 1)
    existing = current.strip()
    entries = []
    if existing:
        chunks = re.split(r"(?m)(?=^## )", existing)
        entries = [chunk.strip() for chunk in chunks if chunk.strip()]

    entries.insert(0, render_entry(payload))
    entries = entries[:10]
    body = "\n\n".join(entries)
    return f"{before}{SESSION_START}\n{body}\n{SESSION_END}{after}"


def update_project_date(original: str, project_id: str, date: str) -> str:
    start_marker = f"<!-- project:{project_id} -->"
    end_marker = f"<!-- /project:{project_id} -->"
    if original.count(start_marker) != 1 or original.count(end_marker) != 1:
        raise ClosureError(f"Projet inconnu ou marqueurs ambigus : {project_id}.")

    before, remainder = original.split(start_marker, 1)
    block, after = remainder.split(end_marker, 1)
    pattern = re.compile(r"(?m)^- Dernière session : .+$")
    if len(pattern.findall(block)) != 1:
        raise ClosureError(f"Champ Dernière session absent ou ambigu pour {project_id}.")
    block = pattern.sub(f"- Dernière session : {date}", block)
    return f"{before}{start_marker}{block}{end_marker}{after}"


def changed_files(root: Path) -> set[str]:
    result = run_git(root, "status", "--porcelain=v1", "--untracked-files=all")
    files: set[str] = set()
    for line in result.stdout.splitlines():
        if len(line) >= 4:
            files.add(line[3:])
    return files


def ensure_repository_ready(root: Path) -> None:
    root = root.resolve()
    top = run_git(root, "rev-parse", "--show-toplevel").stdout.strip()
    if Path(top).resolve() != root:
        raise ClosureError("--repo-root ne correspond pas à la racine Git.")

    branch = run_git(root, "branch", "--show-current").stdout.strip()
    if branch != "main":
        raise ClosureError(f"La clôture exige la branche main, branche actuelle : {branch or 'détachée'}.")

    if changed_files(root):
        raise ClosureError("Le dépôt Jarvis doit être entièrement propre avant la clôture.")

    if run_git(root, "remote", "get-url", "origin", check=False).returncode != 0:
        raise ClosureError("Le remote origin est absent.")
    upstream_result = run_git(
        root, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}", check=False
    )
    if upstream_result.returncode != 0:
        raise ClosureError("La branche main n'a pas d'upstream.")
    if upstream_result.stdout.strip() != "origin/main":
        raise ClosureError(
            f"L'upstream doit être origin/main, valeur actuelle : {upstream_result.stdout.strip()}."
        )

    pull = run_git(root, "pull", "--ff-only", check=False)
    if pull.returncode != 0:
        detail = pull.stderr.strip() or pull.stdout.strip()
        raise ClosureError(f"Synchronisation ff-only impossible : {detail}")
    if changed_files(root):
        raise ClosureError("Le dépôt n'est plus propre après la synchronisation.")


def rollback(root: Path, originals: dict[Path, str], staged: bool) -> None:
    if staged:
        run_git(root, "reset", "--quiet", "HEAD", "--", *[str(path.relative_to(root)) for path in originals], check=False)
    for path, content in originals.items():
        atomic_write(path, content)


def close_session(root: Path, payload: dict[str, str]) -> None:
    root = root.resolve()
    sessions_path = root / "memory/recent-sessions.md"
    projects_path = root / "memory/projects.md"
    for path in (sessions_path, projects_path):
        if not path.is_file():
            raise ClosureError(f"Fichier mémoire absent : {path.relative_to(root)}.")

    ensure_repository_ready(root)

    originals = {
        sessions_path: sessions_path.read_text(encoding="utf-8"),
        projects_path: projects_path.read_text(encoding="utf-8"),
    }
    staged = False
    committed = False

    try:
        new_sessions = update_sessions(originals[sessions_path], payload)
        new_projects = originals[projects_path]
        if payload["scope"] == "project":
            new_projects = update_project_date(new_projects, payload["project_id"], payload["date"])

        atomic_write(sessions_path, new_sessions)
        if new_projects != originals[projects_path]:
            atomic_write(projects_path, new_projects)

        changed = changed_files(root)
        if not changed or not changed.issubset(ALLOWED_MEMORY_FILES):
            raise ClosureError(f"Fichiers modifiés inattendus : {', '.join(sorted(changed)) or 'aucun'}.")

        fetch = run_git(root, "fetch", "--quiet", "origin", check=False)
        if fetch.returncode != 0:
            raise ClosureError(f"Fetch final impossible : {fetch.stderr.strip() or fetch.stdout.strip()}.")
        head = run_git(root, "rev-parse", "HEAD").stdout.strip()
        upstream = run_git(root, "rev-parse", "@{u}").stdout.strip()
        if head != upstream:
            raise ClosureError("Le remote a évolué pendant la clôture ; aucune mémoire n'a été commitée.")

        relative_changed = sorted(changed)
        run_git(root, "add", "--", *relative_changed)
        staged = True
        staged_files = set(filter(None, run_git(root, "diff", "--cached", "--name-only").stdout.splitlines()))
        if staged_files != changed or not staged_files.issubset(ALLOWED_MEMORY_FILES):
            raise ClosureError("Le diff indexé ne correspond pas exactement aux fichiers mémoire autorisés.")
        run_git(root, "diff", "--cached", "--check")

        scope = payload.get("project_id") or "general"
        message = f"chore(memory): close {scope} session {payload['date']}"
        run_git(root, "commit", "-m", message)
        committed = True

        push = run_git(root, "push", "origin", "main", check=False)
        if push.returncode != 0:
            detail = push.stderr.strip() or push.stdout.strip()
            raise ClosureError(
                "La mémoire est commitée localement mais le push a échoué. "
                f"Ne résous rien automatiquement : {detail}"
            )
    except Exception:
        if not committed:
            rollback(root, originals, staged)
        raise

    print("Clôture enregistrée, commitée et poussée avec succès.")


def main() -> int:
    args = parse_args()
    try:
        payload = load_payload(args.input)
        close_session(args.repo_root, payload)
    except ClosureError as exc:
        print(f"Clôture refusée : {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Clôture interrompue par une erreur système : {exc}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
