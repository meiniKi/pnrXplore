
import os
import shutil
import ujson
from pathlib import PosixPath
from .pnrxplore_subpage import PnrXploreSubpage


class PnrXploreArchive:
    def __init__(self):
        self.pages = []

    def add_page(self, page:PnrXploreSubpage):
        self.pages.append(page)

    def archive(self, dst_path: PosixPath):
        os.makedirs(dst_path.with_suffix(""), exist_ok=True)
        pages_dict = [p.archive(dst_path.with_suffix("")) for p in self.pages]
        with open(dst_path.with_suffix("")/"index.json", "w") as f:
            ujson.dump(pages_dict, f)

        shutil.make_archive(
            dst_path.with_suffix(""),
            format='zip',
            root_dir=dst_path.with_suffix(""),
            base_dir=dst_path.with_suffix(""))
        
        shutil.rmtree(dst_path.with_suffix(""))
