#!/usr/bin/env python3
"""Tests locaux sans réseau pour les scripts Jarvis."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent.parent
INSTALL = ROOT / "scripts/install.sh"
SYNC = ROOT / "scripts/sync.sh"
CLOSE = ROOT / "scripts/close-session.py"


def run(
    *args: str | Path,
    check: bool = False,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [str(arg) for arg in args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=env,
    )
    if check and result.returncode != 0:
        raise AssertionError(
            f"Commande en échec ({result.returncode}) : {' '.join(map(str, args))}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return run("git", "-C", repo, *args, check=check)


def init_repo(path: Path) -> None:
    run("git", "init", "-q", "-b", "main", path, check=True)
    git(path, "config", "user.name", "Jarvis Tests")
    git(path, "config", "user.email", "jarvis-tests@example.invalid")
    (path / "README.md").write_text("# Test\n", encoding="utf-8")
    git(path, "add", "README.md")
    git(path, "commit", "-q", "-m", "test: initialize")


def init_remote_pair(base: Path, with_memory: bool = False) -> tuple[Path, Path]:
    remote = base / "remote.git"
    primary = base / "primary"
    run("git", "init", "-q", "--bare", remote, check=True)
    primary.mkdir()
    run("git", "init", "-q", "-b", "main", primary, check=True)
    git(primary, "config", "user.name", "Jarvis Tests")
    git(primary, "config", "user.email", "jarvis-tests@example.invalid")
    (primary / "README.md").write_text("# Test\n", encoding="utf-8")
    if with_memory:
        shutil.copytree(ROOT / "memory", primary / "memory")
    git(primary, "add", ".")
    git(primary, "commit", "-q", "-m", "test: initialize")
    git(primary, "remote", "add", "origin", str(remote))
    git(primary, "push", "-q", "-u", "origin", "main")
    run("git", "--git-dir", remote, "symbolic-ref", "HEAD", "refs/heads/main", check=True)
    return primary, remote


def clone(remote: Path, path: Path) -> None:
    run("git", "clone", "-q", remote, path, check=True)
    git(path, "config", "user.name", "Jarvis Tests")
    git(path, "config", "user.email", "jarvis-tests@example.invalid")


def valid_payload(project_id: str | None = "agroedge") -> dict[str, str]:
    payload = {
        "date": "2026-08-28",
        "scope": "project" if project_id else "general",
        "title": "Validation de la mémoire Jarvis",
        "context": "La session vérifie le fonctionnement du dépôt global et la continuité contrôlée entre plusieurs appareils de Sam.",
        "completed": "Le contrat, les règles de mémoire et les scripts de synchronisation ont été relus puis testés dans des dépôts temporaires isolés.",
        "decisions": "La mémoire reste minimale, partageable et limitée aux résumés ainsi qu'aux dates de dernière session des projets connus.",
        "state": "Le dépôt de test est propre, aligné avec son remote et ne contient aucun changement extérieur au périmètre autorisé.",
        "next": "Relire les résultats, traiter les éventuelles limites signalées puis décider explicitement de l'installation sur le poste professionnel.",
    }
    if project_id:
        payload["project_id"] = project_id
    return payload


def write_payload(path: Path, payload: dict[str, str]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class InstallTests(unittest.TestCase):
    def test_install_creates_verified_link(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            codex_home = Path(temp) / "codex"
            result = run("bash", INSTALL, "--codex-home", codex_home)
            self.assertEqual(result.returncode, 0, result.stderr)
            target = codex_home / "AGENTS.md"
            self.assertTrue(target.is_symlink())
            self.assertEqual(target.resolve(), (ROOT / "AGENTS.md").resolve())

    def test_install_refuses_existing_agents(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            codex_home = Path(temp) / "codex"
            codex_home.mkdir()
            (codex_home / "AGENTS.md").write_text("existant\n", encoding="utf-8")
            result = run("bash", INSTALL, "--codex-home", codex_home)
            self.assertEqual(result.returncode, 4)
            self.assertEqual((codex_home / "AGENTS.md").read_text(encoding="utf-8"), "existant\n")

    def test_install_refuses_override(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            codex_home = Path(temp) / "codex"
            codex_home.mkdir()
            (codex_home / "AGENTS.override.md").write_text("override\n", encoding="utf-8")
            result = run("bash", INSTALL, "--codex-home", codex_home)
            self.assertEqual(result.returncode, 3)
            self.assertFalse((codex_home / "AGENTS.md").exists())

    def test_install_dry_run_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            codex_home = Path(temp) / "codex"
            result = run("bash", INSTALL, "--dry-run", "--codex-home", codex_home)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(codex_home.exists())


class SyncTests(unittest.TestCase):
    def test_sync_refuses_non_main_branch(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo"
            repo.mkdir()
            init_repo(repo)
            git(repo, "checkout", "-q", "-b", "feature/test")
            result = run("bash", SYNC, "--repo-root", repo)
            self.assertEqual(result.returncode, 14)

    def test_sync_refuses_dirty_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo"
            repo.mkdir()
            init_repo(repo)
            (repo / "dirty.txt").write_text("local\n", encoding="utf-8")
            result = run("bash", SYNC, "--repo-root", repo)
            self.assertEqual(result.returncode, 10)

    def test_sync_reports_missing_remote(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo"
            repo.mkdir()
            init_repo(repo)
            result = run("bash", SYNC, "--repo-root", repo)
            self.assertEqual(result.returncode, 11)

    def test_sync_reports_missing_upstream(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            remote = base / "remote.git"
            repo = base / "repo"
            run("git", "init", "-q", "--bare", remote, check=True)
            repo.mkdir()
            init_repo(repo)
            git(repo, "remote", "add", "origin", str(remote))
            result = run("bash", SYNC, "--repo-root", repo)
            self.assertEqual(result.returncode, 12)

    def test_sync_reports_unreachable_remote(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base)
            git(primary, "remote", "set-url", "origin", str(base / "missing.git"))
            result = run("bash", SYNC, "--repo-root", primary)
            self.assertEqual(result.returncode, 13)

    def test_sync_fast_forwards(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, remote = init_remote_pair(base)
            secondary = base / "secondary"
            clone(remote, secondary)
            (secondary / "remote.txt").write_text("remote\n", encoding="utf-8")
            git(secondary, "add", "remote.txt")
            git(secondary, "commit", "-q", "-m", "test: remote change")
            git(secondary, "push", "-q")

            result = run("bash", SYNC, "--repo-root", primary)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((primary / "remote.txt").is_file())

    def test_sync_refuses_divergence(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, remote = init_remote_pair(base)
            secondary = base / "secondary"
            clone(remote, secondary)

            (primary / "local.txt").write_text("local\n", encoding="utf-8")
            git(primary, "add", "local.txt")
            git(primary, "commit", "-q", "-m", "test: local change")
            (secondary / "remote.txt").write_text("remote\n", encoding="utf-8")
            git(secondary, "add", "remote.txt")
            git(secondary, "commit", "-q", "-m", "test: remote change")
            git(secondary, "push", "-q")

            result = run("bash", SYNC, "--repo-root", primary)
            self.assertEqual(result.returncode, 13)
            self.assertFalse((primary / "remote.txt").exists())


class CloseSessionTests(unittest.TestCase):
    def test_close_refuses_missing_remote_without_change(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            repo = base / "repo"
            repo.mkdir()
            init_repo(repo)
            shutil.copytree(ROOT / "memory", repo / "memory")
            git(repo, "add", "memory")
            git(repo, "commit", "-q", "-m", "test: add memory")
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())
            original_sessions = (repo / "memory/recent-sessions.md").read_text(encoding="utf-8")

            result = run("python3", CLOSE, "--repo-root", repo, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            self.assertEqual((repo / "memory/recent-sessions.md").read_text(encoding="utf-8"), original_sessions)
            self.assertEqual(git(repo, "status", "--porcelain").stdout, "")

    def test_close_refuses_missing_upstream_without_change(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base, with_memory=True)
            git(primary, "branch", "--unset-upstream")
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())
            original_sessions = (primary / "memory/recent-sessions.md").read_text(encoding="utf-8")

            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            self.assertEqual((primary / "memory/recent-sessions.md").read_text(encoding="utf-8"), original_sessions)
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")

    def test_close_refuses_unreachable_remote_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base, with_memory=True)
            git(primary, "remote", "set-url", "origin", str(base / "missing.git"))
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())
            original_sessions = (primary / "memory/recent-sessions.md").read_text(encoding="utf-8")

            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            self.assertEqual((primary / "memory/recent-sessions.md").read_text(encoding="utf-8"), original_sessions)
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")

    def test_close_rolls_back_when_final_fetch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base, with_memory=True)
            shim_dir = base / "shim"
            shim_dir.mkdir()
            real_git = shutil.which("git")
            self.assertIsNotNone(real_git)
            shim = shim_dir / "git"
            shim.write_text(
                "#!/bin/sh\n"
                "for argument in \"$@\"; do\n"
                "  if [ \"$argument\" = fetch ]; then exit 42; fi\n"
                "done\n"
                f"exec {real_git} \"$@\"\n",
                encoding="utf-8",
            )
            shim.chmod(0o755)
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())
            original_sessions = (primary / "memory/recent-sessions.md").read_text(encoding="utf-8")
            original_projects = (primary / "memory/projects.md").read_text(encoding="utf-8")
            test_env = dict(os.environ)
            test_env["PATH"] = f"{shim_dir}{os.pathsep}{test_env['PATH']}"

            result = run(
                "python3", CLOSE, "--repo-root", primary, "--input", payload_path, env=test_env
            )
            self.assertEqual(result.returncode, 2)
            self.assertEqual((primary / "memory/recent-sessions.md").read_text(encoding="utf-8"), original_sessions)
            self.assertEqual((primary / "memory/projects.md").read_text(encoding="utf-8"), original_projects)
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")
    def test_close_updates_only_authorized_memory_and_pushes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, remote = init_remote_pair(base, with_memory=True)
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())

            before = git(primary, "rev-parse", "HEAD").stdout.strip()
            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 0, result.stderr)
            after = git(primary, "rev-parse", "HEAD").stdout.strip()
            self.assertNotEqual(before, after)
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")
            self.assertIn("## 2026-08-28 — agroedge", (primary / "memory/recent-sessions.md").read_text(encoding="utf-8"))
            self.assertIn("- Dernière session : 2026-08-28", (primary / "memory/projects.md").read_text(encoding="utf-8"))
            remote_head = run("git", "--git-dir", remote, "rev-parse", "refs/heads/main", check=True).stdout.strip()
            self.assertEqual(after, remote_head)
            changed = git(primary, "show", "--pretty=format:", "--name-only", "HEAD").stdout.split()
            self.assertEqual(set(changed), {"memory/projects.md", "memory/recent-sessions.md"})

    def test_close_general_does_not_touch_projects(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base, with_memory=True)
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload(project_id=None))
            original_projects = (primary / "memory/projects.md").read_text(encoding="utf-8")

            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((primary / "memory/projects.md").read_text(encoding="utf-8"), original_projects)
            changed = git(primary, "show", "--pretty=format:", "--name-only", "HEAD").stdout.split()
            self.assertEqual(changed, ["memory/recent-sessions.md"])

    def test_close_refuses_unknown_project_without_change(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base, with_memory=True)
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload(project_id="inconnu"))
            before = git(primary, "rev-parse", "HEAD").stdout.strip()

            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(git(primary, "rev-parse", "HEAD").stdout.strip(), before)
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")

    def test_close_refuses_dirty_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base, with_memory=True)
            (primary / "dirty.txt").write_text("ne pas toucher\n", encoding="utf-8")
            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())

            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            self.assertTrue((primary / "dirty.txt").is_file())

    def test_close_rotates_fifo_to_ten_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, remote = init_remote_pair(base, with_memory=True)
            sessions = primary / "memory/recent-sessions.md"
            entries = "\n\n".join(
                f"## 2026-08-{day:02d} — général — session-{index}\n\n- Contexte : entrée historique."
                for index, day in enumerate(range(10, 20))
            )
            text = sessions.read_text(encoding="utf-8")
            text = text.replace("<!-- sessions:start -->\n<!-- sessions:end -->", f"<!-- sessions:start -->\n{entries}\n<!-- sessions:end -->")
            sessions.write_text(text, encoding="utf-8")
            git(primary, "add", "memory/recent-sessions.md")
            git(primary, "commit", "-q", "-m", "test: seed fifo")
            git(primary, "push", "-q")

            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload(project_id=None))
            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 0, result.stderr)
            final = sessions.read_text(encoding="utf-8")
            self.assertEqual(final.count("\n## "), 10)
            self.assertNotIn("session-9", final)
            remote_head = run("git", "--git-dir", remote, "rev-parse", "refs/heads/main", check=True).stdout.strip()
            self.assertEqual(git(primary, "rev-parse", "HEAD").stdout.strip(), remote_head)

    def test_close_refuses_secret_like_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, _ = init_remote_pair(base, with_memory=True)
            payload = valid_payload()
            payload["context"] += " api_key=super-secret-value"
            payload_path = base / "session.json"
            write_payload(payload_path, payload)

            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")

    def test_close_refuses_remote_divergence_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, remote = init_remote_pair(base, with_memory=True)
            secondary = base / "secondary"
            clone(remote, secondary)

            (primary / "local.txt").write_text("local\n", encoding="utf-8")
            git(primary, "add", "local.txt")
            git(primary, "commit", "-q", "-m", "test: local divergence")
            (secondary / "remote.txt").write_text("remote\n", encoding="utf-8")
            git(secondary, "add", "remote.txt")
            git(secondary, "commit", "-q", "-m", "test: remote divergence")
            git(secondary, "push", "-q")

            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())
            original_sessions = (primary / "memory/recent-sessions.md").read_text(encoding="utf-8")
            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(
                (primary / "memory/recent-sessions.md").read_text(encoding="utf-8"),
                original_sessions,
            )
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")

    def test_close_keeps_local_commit_when_push_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary, remote = init_remote_pair(base, with_memory=True)
            hook = remote / "hooks/pre-receive"
            hook.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
            hook.chmod(0o755)

            payload_path = base / "session.json"
            write_payload(payload_path, valid_payload())
            before = git(primary, "rev-parse", "HEAD").stdout.strip()
            result = run("python3", CLOSE, "--repo-root", primary, "--input", payload_path)
            self.assertEqual(result.returncode, 2)
            after = git(primary, "rev-parse", "HEAD").stdout.strip()
            self.assertNotEqual(before, after)
            self.assertEqual(git(primary, "status", "--porcelain").stdout, "")
            remote_head = run("git", "--git-dir", remote, "rev-parse", "refs/heads/main", check=True).stdout.strip()
            self.assertEqual(remote_head, before)
            self.assertIn("commitée localement", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
