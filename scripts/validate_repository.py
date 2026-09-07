"""Validate this workflow distribution using the Python standard library."""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("research-result-trace", "research-display-revision")


def validate():
    checks = []

    def check(name, passed, detail=None):
        checks.append({"check": name, "passed": bool(passed), "detail": detail})

    files = sorted(p for p in ROOT.rglob("*") if p.is_file()
                   and not {".git", "__pycache__", ".venv", ".agents", "local_results"}.intersection(p.relative_to(ROOT).parts))
    check("required_entrypoints", all((ROOT / p).is_file() for p in
          ["README.md", "WORKFLOW.md", "AGENTS.md", "LICENSE", "docs/usage.md"]))
    bad_links = []
    for path in (p for p in files if p.suffix == ".md"):
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if re.match(r"https?://|mailto:|#", link):
                continue
            target = (path.parent / link.strip("<>").split("#")[0]).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                bad_links.append({"file": path.relative_to(ROOT).as_posix(), "target": link})
    check("local_links_resolve_inside_repository", not bad_links, bad_links)

    fingerprints = json.loads((ROOT / "validation/skill_fingerprints.json").read_text(encoding="utf-8"))["files"]
    actual = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in files if p.relative_to(ROOT).parts[0] == "skills"}
    check("tested_skill_files_match_exact_fingerprints", actual == fingerprints)
    check("exactly_two_focused_skills", sorted(p.name for p in (ROOT / "skills").iterdir()) == sorted(SKILLS))
    for name in SKILLS:
        text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", text)
        # 此处只接受当前两字段单行 frontmatter，不声称完成通用 YAML 校验。
        okay = (match is not None and match.group(1) == name
                and 0 < len(match.group(2)) <= 1024 and ": " not in match.group(2))
        check(f"simple_frontmatter:{name}", okay)

    contract = ROOT / "templates/research-project/config/study_contract.yaml"
    fields = dict(line.split(":", 1) for line in contract.read_text(encoding="utf-8").splitlines() if line.strip())
    check("template_has_no_scientific_defaults", all(value.strip() in {"null", "[]", "{}"}
          for key, value in fields.items() if key not in {"contract_version", "contract_status"}))
    check("template_is_draft", fields.get("contract_status", "").strip() == "draft")
    leaks = []
    for path in files:
        if path.suffix not in {".md", ".csv", ".yaml", ".json"}:
            continue
        text = path.read_text(encoding="utf-8-sig")
        if re.search(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|/(?:Users|home)/[^<\s]+|\b[ED]\d{2}\b|GCST\d+|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}", text):
            leaks.append(path.relative_to(ROOT).as_posix())
    check("no_obvious_machine_paths_private_evidence_ids_or_tokens", not leaks, leaks)
    unexpected = [p.relative_to(ROOT).as_posix() for p in files
                  if p.suffix not in {".md", ".py", ".json", ".csv", ".yaml"}
                  and p.name not in {"LICENSE", ".gitignore", ".gitattributes"}]
    check("distribution_contains_only_expected_text_formats", not unexpected, unexpected)
    check("six_playbooks_present", len(list((ROOT / "playbooks").glob("0*.md"))) == 6)
    check("example_is_marked_synthetic", "虚拟" in (ROOT / "examples/README.md").read_text(encoding="utf-8"))
    return {"passed": all(row["passed"] for row in checks), "check_count": len(checks), "checks": checks}


if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
