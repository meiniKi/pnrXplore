import os
import shutil
import logging
from pathlib import PosixPath
from .pnrxplore_template_page import PnrXploreTemplatePage
from typing import Dict, List
from dataclasses import dataclass


class PnrXploreOverview(PnrXploreTemplatePage):
    def __init__(self, label: str, key: str, title: str | None = None):
        super().__init__(label, key, title)
        self.sections: List[Dict] = []

    def add_section(self, title, data, column_config={}):
        self.sections.append(
            {"title": title, "data": data, "column_config": column_config}
        )

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent / self.key, exist_ok=True)
        return super().archive_with(parent, self.asdict())

    def asdict(self):
        return self.__class__.__name__, [{"sections": self.sections}]
