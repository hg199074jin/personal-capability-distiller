"""Safe Obsidian capability archive core.

写入采用独占创建模式（``open(..., "x")``）并以 UTF-8 编码、LF 换行落盘。
归档操作允许新建笔记和索引，但绝不覆盖已存在且内容不同的笔记，
也不删除或静默合并既有资料。
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path

import yaml


class AssetKind(str, Enum):
    SOURCE = "source"
    DISTILLATION = "distillation"
    CAPABILITY_CARD = "capability_card"
    SKILL_CANDIDATE = "skill_candidate"
    SKILL_VALIDATED = "skill_validated"
    SIMULATION = "simulation"
    APPLICATION_FEEDBACK = "application_feedback"


@dataclass(frozen=True)
class ArchiveRequest:
    asset_id: str
    title: str
    kind: AssetKind
    primary_domain: str
    auxiliary_domains: tuple[str, ...]
    depth: str
    workflow_state: str
    maturity: str
    source_links: tuple[str, ...]
    tags: tuple[str, ...]
    relationships: tuple[str, ...]
    content_origin: str
    skill_version: str
    validation_status: str
    body: str


@dataclass(frozen=True)
class ArchiveResult:
    path: Path
    created: bool
    unchanged: bool


FOLDER_BY_KIND = {
    AssetKind.SOURCE: "01_来源资料",
    AssetKind.DISTILLATION: "02_蒸馏记录",
    AssetKind.CAPABILITY_CARD: "03_能力卡片",
    AssetKind.SKILL_CANDIDATE: "04_Skill候选",
    AssetKind.SKILL_VALIDATED: "05_Skill已验证",
    AssetKind.SIMULATION: "06_测试记录",
    AssetKind.APPLICATION_FEEDBACK: "07_应用反馈",
}

REQUIRED_DIRECTORIES = (
    "00_能力地图",
    "01_来源资料",
    "02_蒸馏记录",
    "03_能力卡片",
    "04_Skill候选",
    "05_Skill已验证",
    "06_测试记录",
    "07_应用反馈",
    "90_模板与配置",
)


def safe_filename(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value).strip(" .")
    return cleaned[:80] or "untitled"


def render_note(request: ArchiveRequest) -> str:
    frontmatter = asdict(request)
    frontmatter["kind"] = request.kind.value
    frontmatter.pop("body")
    for key in ("auxiliary_domains", "source_links", "tags", "relationships"):
        frontmatter[key] = list(frontmatter[key])
    header = yaml.safe_dump(
        frontmatter,
        allow_unicode=True,
        sort_keys=False,
    ).strip()
    return f"---\n{header}\n---\n\n{request.body.rstrip()}\n"


def write_new_utf8(target: Path, content: str) -> None:
    with target.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(content)
        handle.flush()


def archive_asset(vault_root: Path, request: ArchiveRequest) -> ArchiveResult:
    folder = vault_root / FOLDER_BY_KIND[request.kind]
    folder.mkdir(parents=True, exist_ok=True)
    filename = (
        f"{request.asset_id}_{safe_filename(request.title)}"
        f"_v{request.skill_version}.md"
    )
    target = folder / filename
    rendered = render_note(request)
    if target.exists():
        if target.read_text(encoding="utf-8") == rendered:
            return ArchiveResult(target, created=False, unchanged=True)
        raise FileExistsError(
            f"Refusing to overwrite different content: {target}"
        )
    write_new_utf8(target, rendered)
    return ArchiveResult(target, created=True, unchanged=False)


def check_vault(vault_root: Path) -> list[str]:
    """Return missing required directories without creating or modifying anything."""
    missing: list[str] = []
    for name in REQUIRED_DIRECTORIES:
        if not (vault_root / name).is_dir():
            missing.append(name)
    return missing


def _load_request(path: Path) -> ArchiveRequest:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    data["kind"] = AssetKind(data["kind"])
    return ArchiveRequest(**data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Safely archive a capability asset into an Obsidian vault."
    )
    parser.add_argument("--vault-root", required=True, type=Path)
    parser.add_argument("--request", type=Path, help="path to a request YAML file")
    parser.add_argument(
        "--check-vault",
        action="store_true",
        help="report missing required directories without writing",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="only preview what would happen; do not write",
    )
    args = parser.parse_args(argv)

    if args.check_vault:
        missing = check_vault(args.vault_root)
        if missing:
            print("[check-vault] 缺失目录:")
            for name in missing:
                print(f"  - {name}")
        else:
            print("[check-vault] 八个必需目录齐全。")
        print("[check-vault] dry-run: 未创建或修改任何文件。")
        return 0

    if not args.request:
        parser.error("--request is required unless --check-vault is set")

    request = _load_request(args.request)
    folder = args.vault_root / FOLDER_BY_KIND[request.kind]
    filename = (
        f"{request.asset_id}_{safe_filename(request.title)}"
        f"_v{request.skill_version}.md"
    )
    target = folder / filename
    print(f"[preview] 目标: {target}")
    print(f"[preview] kind: {request.kind.value} | state: {request.workflow_state}")
    if target.exists():
        print("[preview] 目标已存在；相同内容将保持幂等，不同内容将拒绝覆盖。")
    if args.dry_run:
        print("[preview] dry-run: 未写入任何文件。")
        return 0

    result = archive_asset(args.vault_root, request)
    print(
        f"[done] created={result.created} unchanged={result.unchanged} "
        f"path={result.path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
