from pathlib import PosixPath


class PnrXploreControl:
    """Abstract class for all control components, e.g., components that select
    the state to be visualized."""
    component_type = "control"

    def archive(self, parent: PosixPath) -> str:
        NotImplementedError(f"Abstract class {self.__class__.__name__}")

    def __init__(self):
        pass
