import os
import shutil
from pathlib import PosixPath
from pnrxplore_template import PnrXploreTemplate


class PnrXploreCinema(PnrXploreTemplate):
    def __init__(self):
        self.data = list()

    def add_video(self, title: str, file: str, rel_path: str):
        self.data.append((title, file, rel_path))

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent, exist_ok=True)
        for e in self.data:
            shutil.copy(e[1], parent / e[2])
        return self.asdict()

    def asdict(self):
        return self.component_type, [{e[0]: e[2] for e in self.data}]
