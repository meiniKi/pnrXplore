import os
import shutil
import logging
from pathlib import PosixPath
from .pnrxplore_template_page import PnrXploreTemplatePage


class PnrXploreNextpnrViewer(PnrXploreTemplatePage):
    """A page embedding the nextpnr viewer to visualize the target
    FPGA architecture and implemented design."""""
    def __init__(
        self,
        label: str,
        key: str,
        title: str | None = None,
        family: str = "",
        device: str = "",
        json_file: PosixPath = "",
    ):
        logging.warning("PnrXploreNextpnrViewer is experimental!")
        super().__init__(label, key, title)
        self.family = family
        self.device = device
        self.json_file = json_file

    def archive(self, parent: PosixPath) -> str:
        os.makedirs(parent / self.key, exist_ok=True)
        shutil.copy(self.json_file, parent / self.key / self.json_file.name)
        return super().archive_with(parent, self.asdict())

    def asdict(self):
        return self.__class__.__name__, [
            {
                "json_file": self.json_file.name,
                "family": self.family,
                "device": self.device,
            }
        ]
