import os
import shutil
import logging
from pathlib import PosixPath
from .pnrxplore_template_page import PnrXploreTemplatePage
from typing import Dict, List
from dataclasses import dataclass, asdict


class PnrXploreOverview(PnrXploreTemplatePage):
    @dataclass
    class Table:
        title: str
        data: Dict
        column_config: Dict

        def archive(self, parent: PosixPath):
            pass

    @dataclass
    class Markdown:
        md: str
        files: List[PosixPath | str]

        def archive(self, parent: PosixPath):
            for f in self.files:
                shutil.copy(f, parent / f.name)
            self.files = [f.name for f in self.files]

    def __init__(self, label: str, key: str, title: str | None = None):
        super().__init__(label, key, title)
        self.sections: List[PnrXploreOverview.Table | PnrXploreOverview.Markdown] = []

    def add_section(self, title, data, column_config={}):
        logging.warning("add_section will be removed, use add_table")
        self.add_table(title, data, column_config)

    def add_table(self, title: str, data, column_config={}):
        self.sections.append(
            PnrXploreOverview.Table(title=title, data=data, column_config=column_config)
        )

    def add_markdown(self, md: str, files: List[PosixPath] = list()):
        self.sections.append(PnrXploreOverview.Markdown(md=md, files=files))

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent / self.key, exist_ok=True)
        for s in self.sections:
            s.archive(parent)
        return super().archive_with(parent, self.asdict())

    def asdict(self):
        return self.__class__.__name__, [
            {
                "sections": [
                    {"id": s.__class__.__name__} | asdict(s) for s in self.sections
                ]
            }
        ]
