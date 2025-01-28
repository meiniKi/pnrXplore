
from pathlib import PosixPath
from typing import List
from .pnrxplore_dash_item import PnrXploreDashItem


class PnrXploreDashboard:
    element_type = "dashboard"
    def __init__(self):
        self.items: List[PnrXploreDashItem] = []

    def archive(self, parent:PosixPath):
        for i in self.items:
            i.archive(parent)
        return self.asdict()

    def add_item(self, item:PnrXploreDashItem):
        self.items.append(item)

    def asdict(self):
        return self.element_type, [i.asdict() for i in self.items]