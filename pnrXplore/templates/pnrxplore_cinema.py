import os
import shutil
from pathlib import PosixPath
from .pnrxplore_template_page import PnrXploreTemplatePage


class PnrXploreCinema(PnrXploreTemplatePage):
    """Page to display video renderings."""
    def __init__(self, label: str, key: str, title: str | None = None):
        super().__init__(label, key, title)
        self.data = list()

    def add_video(self, title: str, file: str, rel_path: str):
        self.data.append((title, file, rel_path))

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent / self.key, exist_ok=True)
        for e in self.data:
            shutil.copy(e[1], parent / self.key / e[2])
        return super().archive_with(parent, self.asdict())

    def asdict(self):
        return self.__class__.__name__, [{e[0]: e[2] for e in self.data}]
