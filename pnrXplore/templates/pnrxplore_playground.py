import os
import shutil
import logging
from pathlib import PosixPath
from .pnrxplore_template_page import PnrXploreTemplatePage


class PnrXplorePlayground(PnrXploreTemplatePage):
    """Template for a Python playground page. Notes that this is highly insecure in
        unrusted environments. Requires sandboxing."""
    def __init__(self, label: str, key: str, title: str | None = None, code: str = ""):
        logging.warning(
            "PnrXplorePlayground currently is highly insecure if run in an untrusted environment!"
        )
        super().__init__(label, key, title)
        self.code = code
        self.path = "code.py"

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent / self.key, exist_ok=True)
        with open(parent / self.key / self.path, "w") as f:
            f.write(self.code)
        return super().archive_with(parent, self.asdict())

    def asdict(self):
        return self.__class__.__name__, [{"file": self.path}]
