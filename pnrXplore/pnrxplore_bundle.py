import os
import shutil
import ujson
from pathlib import PosixPath
from typing import Literal
from .pnrxplore_page import PnrXplorePage
from .templates import PnrXploreTemplatePage


class PnrXploreBundle:
    def __init__(self):
        self.pages = []

    def add_page(self, page: PnrXplorePage | PnrXploreTemplatePage):
        self.pages.append(page)

    def archive(self, dst_path: PosixPath, format: Literal["zip"] | Literal["tar"]):
        os.makedirs(dst_path.with_suffix(""), exist_ok=True)
        pages_dict = [p.archive(dst_path.with_suffix("")) for p in self.pages]
        with open(dst_path.with_suffix("") / "index.json", "w") as f:
            ujson.dump(pages_dict, f)

        shutil.make_archive(
            dst_path.with_suffix(""),
            format=format,
            root_dir=dst_path.with_suffix(""),
        )

        shutil.rmtree(dst_path.with_suffix(""))
