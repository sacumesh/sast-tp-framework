from pathlib import Path
from typing import Dict

import core.utils
from core import utils

import sast.sast_tools as sast_tools


async def scan(src_dir: Path, tools: list[Dict], language: str, modelling_rules: Path = None):
    if not src_dir.is_dir():
        raise
    if not tools:
        raise

    results = []
    for tool in tools:
        sast = sast_tools.get_sast_tool(tool["name"], tool["version"])
        res = await sast.launcher(src_dir, language, output_dir, use_mvn=(src_dir / "pom.xml").exists(),
                                  apply_remediation=True, modelling_rules=modelling_rules)

        results.append({f"{tool['name']}:{tool['version']}": sast.inspector(res, language)})
    return results, tools
