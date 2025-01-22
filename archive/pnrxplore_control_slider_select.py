
from typing import List, Dict
from pathlib import PosixPath
from .pnrxplore_control import PnrXploreControl

class PnrXploreControlSliderSelect(PnrXploreControl):
    def __init__(self, label:str, key:str, options:List[str|float|int]|None=None):
        self.label = label
        self.key = key
        self.options = options

    def archive(self, parent:PosixPath) -> Dict:
        return self.asdict()

    def asdict(self):
        return self.element_type, [{"type": self.__class__.__name__,
                                    "label": self.label,
                                    "key": self.key,
                                    "options": self.options}]