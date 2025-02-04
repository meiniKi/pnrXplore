import os
from pathlib import PosixPath
import ujson
import logging
from .controls import *
from .dashboard import *
from .templates import *


class PnrXploreSubpage:
    def __init__(self, label: str, key: str, title: str | None = None):
        self.label = label
        self.key = key
        self.title = title
        self.components = []

    def add_component(self, component: PnrXploreControl | PnrXploreDashboard):
        self.components.append(component)

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent / self.key, exist_ok=True)

        d = dict()
        for component in self.components:
            type_content = component.archive(parent / self.key)
            (component_type, content) = type_content
            if not component_type in d:
                d[component_type] = list()
            d[component_type] += content

        with open(parent / self.key / "data.json", "w") as f:
            ujson.dump(
                {
                    "key": self.key,
                    "title": self.title,
                    "type": "constructed",
                    "components": d,
                },
                f,
                indent=4,
            )
        return {"key": self.key, "title": self.title}
