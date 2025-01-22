
from pathlib import PosixPath

class PnrXploreDashItem:
    def __init__(self, label:str, key:str, x:int, y:int, w:int, h:int, dragable:bool, resizable:bool):
        self.key = key
        self.label = label
        self.layout = {
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "isDraggable": dragable,
            "isResizable": resizable}
        
    def archive(self, parent:PosixPath) -> str:
        NotImplementedError(f"Abstract class {self.__class__.__name__}") 

    def asdict(self):
        return {"key": self.key, "layout": self.layout, "item_type": {}, "item_content": {}}