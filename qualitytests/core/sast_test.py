import asyncio
from pathlib import Path
from typing import Dict

from SAST.src.sast import SAST


class SastTest(SAST):
    async def launcher(self, src_dir: Path, language: str, output_dir: Path, **kwargs) -> Path:
        await asyncio.sleep(0.5)
        return src_dir / f"{src_dir.name}.csv"

    def inspector(self, sast_res_file: Path, language: str) -> list[Dict]:
        return [
            {
                "type": "xss",
                "file": "/path/to/dummy.php",
                "line": 23
            }
        ]

    async def get_tool_version(self) -> str:
        pass

    def logger(self) -> None:
        pass


class SastTestException(SAST):
    async def launcher(self, src_dir: Path, language: str, output_dir: Path, **kwargs) -> Path:
        await asyncio.sleep(0.5)
        raise Exception("whatever")

    def inspector(self, sast_res_file: Path, language: str) -> list[Dict]:
        return [
            {
                "type": "xss",
                "file": "/path/to/dummy.php",
                "line": 23
            }
        ]

    async def get_tool_version(self) -> str:
        pass

    def logger(self) -> None:
        pass