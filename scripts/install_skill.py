"""Copy one selected skill to an explicit skills directory without overwriting."""

import argparse
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("research-result-trace", "research-display-revision")


def install(name, destination):
    if name not in SKILLS:
        raise ValueError("Select one of the two supported skills.")
    source = ROOT / "skills" / name
    target = Path(destination).expanduser().resolve() / name
    # 拒绝普通目录和失效符号链接，避免覆盖既有安装。
    if target.exists() or target.is_symlink():
        raise FileExistsError(f"Destination already exists; left unchanged: {target}")
    if not (source / "SKILL.md").is_file():
        raise FileNotFoundError("The selected source skill is incomplete.")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", choices=SKILLS)
    parser.add_argument("--destination", required=True, type=Path,
                        help="Skills parent directory; for example ~/.agents/skills")
    args = parser.parse_args()
    try:
        target = install(args.name, args.destination)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Installation not completed: {exc}\n")
    print(json.dumps({"skill": args.name, "installed_to": str(target)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
