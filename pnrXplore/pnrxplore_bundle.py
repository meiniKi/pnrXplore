import os
import shutil
import ujson
from pathlib import PosixPath
from typing import Literal
from .pnrxplore_page import PnrXplorePage
from .templates import PnrXploreTemplatePage


class PnrXploreBundle:
    """The bundle of all data and visualization descriptions, i.e., allocated pages and components."""
    def __init__(self):
        self.pages = []
        self.tmp_folder = None

    def add_page(self, page: PnrXplorePage | PnrXploreTemplatePage):
        self.pages.append(page)

    def archive(
        self,
        dst_path: PosixPath,
        format: Literal["zip"] | Literal["tar"],
        keep_tmp: bool = False,
    ):
        self.tmp_folder = dst_path.parent / "tmp_{}".format(os.urandom(8).hex())
        os.makedirs(self.tmp_folder, exist_ok=False)
        pages_dict = [p.archive(self.tmp_folder) for p in self.pages]
        with open(self.tmp_folder / "index.json", "w") as f:
            ujson.dump(pages_dict, f)

        shutil.make_archive(
            base_name=dst_path.with_suffix(""),
            format=format,
            root_dir=self.tmp_folder,
        )

        if not keep_tmp:
            shutil.rmtree(self.tmp_folder)
