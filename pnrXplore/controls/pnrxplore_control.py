from pathlib import PosixPath


class PnrXploreControl:
    component_type = "control"

    def archive(self, parent: PosixPath) -> str:
        NotImplementedError(f"Abstract class {self.__class__.__name__}")

    def __init__(self):
        pass
