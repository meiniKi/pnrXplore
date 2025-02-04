import os
import shutil
from pathlib import PosixPath
from .pnrxplore_template_page import PnrXploreTemplatePage


class PnrXploreNotes(PnrXploreTemplatePage):
    def __init__(
        self, label: str, key: str, title: str | None = None, markdown: str = ""
    ):
        super().__init__(label, key, title)
        self.markdown = markdown
        self.path = "text.md"

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent / self.key, exist_ok=True)
        with open(parent / self.key / self.path, "w") as f:
            f.write(self.markdown)
        return super().archive_with(parent, self.asdict())

    def asdict(self):
        return self.__class__.__name__, [{"file": self.path}]
