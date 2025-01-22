
import os
import shutil
from typing import List
from .pnrxplore_dash_item import PnrXploreDashItem
from pathlib import PosixPath


class PnrXploreDashStateImage(PnrXploreDashItem):
    def __init__(self, images:List[PosixPath], format_template: str, format_keys: List[tuple], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.images = images
        self.format_template = self.key+"/"+format_template
        self.format_keys = format_keys

    def archive(self, parent:PosixPath) -> str:
        os.makedirs(parent/self.key, exist_ok=True)
        for image in self.images:
            shutil.copy(image, parent/self.key)

    def asdict(self):
        return {"key": self.key,
                "layout": self.layout,
                "item_type": self.__class__.__name__,
                "item_content": { "relpath_template": self.format_template,
                                  "format_keys": self.format_keys}
                }