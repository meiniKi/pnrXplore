
import os
from pathlib import PosixPath
import ujson
from .pnrxplore_control import PnrXploreControl
from .pnrxplore_dashboard import PnrXploreDashboard
from .pnrxplore_video_select import PnrXploreVideoSelect


class PnrXploreSubpage:
    def __init__(self, label:str, key:str, title:str|None=None):
        self.label = label
        self.key = key
        self.title = title
        self.elements = []

    def add_element(self, element: PnrXploreControl|PnrXploreDashboard|PnrXploreVideoSelect):
        self.elements.append(element)

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent/self.key, exist_ok=True)

        d = dict()
        for element in self.elements:
            type_content = element.archive(parent/self.key)
            (element_type, content) = type_content
            if not element_type in d:
                d[element_type] = list()
            d[element_type] += content

        with open(parent/self.key/"data.json", "w") as f:
            ujson.dump({"key": self.key, "title": self.title, "elements": d}, f, indent=4)

        return {"key": self.key, "title": self.title}

