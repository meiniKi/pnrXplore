
from pathlib import PosixPath

class PnrXploreControl:
    element_type = "controls" 

    def archive(self, parent:PosixPath) -> str:
        NotImplementedError(f"Abstract class {self.__class__.__name__}") 
    
    def __init__(self):
        pass