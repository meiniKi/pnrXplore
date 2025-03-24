from typing import Literal, Dict
from pathlib import PosixPath
import os
import ujson


class PnrXploreTemplatePage:
    """Basis class for all templated pages."""
    def __init__(self, label: str, key: str, title: str | None = None):
        self.label = label
        self.key = key
        self.title = title

    def archive(self, parent: PosixPath) -> str:
        raise NotImplementedError

    def archive_with(self, parent: PosixPath, data) -> str:
        with open(parent / self.key / "data.json", "w") as f:
            ujson.dump(
                {
                    "key": self.key,
                    "title": self.title,
                    "type": "template",
                    "data": data,
                },
                f,
                indent=4,
            )
        return {"key": self.key, "title": self.title}
