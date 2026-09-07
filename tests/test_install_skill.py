"""Exercise actual installation and refusal behavior in isolated directories."""

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/install_skill.py"
spec = importlib.util.spec_from_file_location("workflow_installer", SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


def fingerprint(directory):
    return {p.relative_to(directory).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in directory.rglob("*") if p.is_file()}


class InstallSkillTests(unittest.TestCase):
    def test_each_skill_copies_exact_bytes_into_path_with_spaces(self):
        with tempfile.TemporaryDirectory() as temp:
            parent = Path(temp) / "project with spaces" / ".agents" / "skills"
            for name in installer.SKILLS:
                result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), name, "--destination", str(parent)],
                                        capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["skill"], name)
                self.assertEqual(fingerprint(parent / name), fingerprint(ROOT / "skills" / name))

    def test_existing_installation_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            target = installer.install(installer.SKILLS[0], temp)
            (target / "local_note.md").write_text("Keep this local customization.", encoding="utf-8")
            before = fingerprint(target)
            with self.assertRaises(FileExistsError):
                installer.install(installer.SKILLS[0], temp)
            self.assertEqual(before, fingerprint(target))

    def test_unknown_skill_creates_no_destination(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "untouched"
            with self.assertRaises(ValueError):
                installer.install("../unexpected", destination)
            self.assertFalse(destination.exists())

    def test_cli_requires_explicit_destination(self):
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), installer.SKILLS[0]],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--destination", result.stderr)


if __name__ == "__main__":
    unittest.main()
