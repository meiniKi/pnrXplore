
import os
import shutil
from typing import List, Dict, Optional
from .pnrxplore_dash_item import PnrXploreDashItem
from dataclasses import dataclass
from pathlib import PosixPath


class PnrXploreDashVideo(PnrXploreDashItem):
    def __init__(self, file:PosixPath, *args, **kwargs):
        super().__init__(*args, **kwargs)
      

    def archive(self, parent:PosixPath) -> str:
        pass

        return {"label": self.label,
                "key": self.key,
                "layout": self.layout,
                "item_type": self.__class__.__name__,
                "item_content": None}
