
import os
import shutil
from typing import List, Dict
from .pnrxplore_dash_item import PnrXploreDashItem
from dataclasses import dataclass
from pathlib import PosixPath


class PnrXploreDashLine(PnrXploreDashItem):
   
    @dataclass
    class Margin():
        top: int
        right: int
        bottom: int
        left: int

    @dataclass
    class Axis():
        tickSize: int
        tickPadding: int
        tickRotation: int
        legend: str
        legendOffset: int
        legendPosition: str
        tickValues: List

    @dataclass
    class Scale():
        type: str
        min: str
        max: str
        stacked: bool
        reverse: bool

    def __init__(self, data_key:str|None=None, color: str|None=None, data: Dict|None=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = []
        if color is not None and data is not None:
            self.add_trace(data_key, color, data)
        self.options = dict()
        self.set_option("margin", self.Margin(top=10, right=10, bottom=80, left=60))
        self.line_width = 2
        self.curve = "linear"
        self.enable_points = False
        self.enable_xgrid = False
        self.enable_ygrid = True

    def add_trace(self, data_key: str, color: str, data: Dict):
        self.data.append({"id": data_key, "color": color, "data": data})

    def __auto_set_xaxis(self):
        self.set_option("axisBottom", self.Axis(
            tickSize=10,
            tickPadding=1,
            tickRotation=0,
            legend='',
            legendOffset=50,
            legendPosition='middle',
            tickValues=list(range(0, len(self.data[-1]["data"])+1, 100))
        ))

    def __auto_set_yaxis(self):
        self.set_option("axisLeft", self.Axis(
            tickSize=10,
            tickPadding=1,
            tickRotation=0,
            legend=self.label,
            legendOffset=50,
            legendPosition='middle',
            tickValues=list(range(0, len(self.data[-1]["data"])+1, 100))
        ))

    def __auto_set_xscale(self):
        self.set_option("xScale", self.Scale(
            type="point",
            min="auto",
            max="auto",
            stacked=True,
            reverse=False
        ))

    def __auto_set_yscale(self):
        self.set_option("yScale", self.Scale(
            type="linear",
            min="0",
            max="auto",
            stacked=True,
            reverse=False
        ))

    def set_option(self, key, option):
        self.options[key] = vars(option)

    def set_line_width(self, width: int=4):
        self.line_width = width

    def archive(self, parent:PosixPath) -> str:
        pass

    def asdict(self):
        if not "axisBottom" in self.options:
            self.__auto_set_xaxis()
        if not "leftBottom" in self.options:
            self.__auto_set_yaxis()
        if not "yScale" in self.options:
            self.__auto_set_yscale()
        if not "xScale" in self.options:
            self.__auto_set_xscale()

        # TODO: add further options setable if required
        # TODO: generalize for other style plots

        legends_dict = dict()
        if len(self.data) > 1:
            legends_dict = {"legends": [{
                            "anchor": "bottom",
                            "direction": "row",
                            "itemHeight": 20,
                            "itemWidth": 80,
                            "toggleSerie": True,
                            "translateY": 50}]}

        theme_dict = {"theme": {
                        "crosshair": {
                            "line": {
                            "strokeWidth": 2,
                            "stroke": "#007d74",
                            "strokeOpacity": 1}},
                        "tooltip": {
                            "container": {
                                "background": "#043b37",
                                "color": "white",
                                "fontSize": 10 }},
                        "axis": {"legend": {"text": {"fill": "#dbb572",
                                                     "fontSize": 14}},
                                 "ticks": {"text": {"fill": "#b5b5b5"}}}
                        }
                    }

        item_content_dict = {
            "data": self.data,
            "lineWidth": self.line_width,
            "isInteractive": True,
            "enableTouchCrosshair": True,
            "crosshairType": "cross",
            "useMesh": True,
            "curve": self.curve,
            "textColor": "#c4c4c4",
            "enablePoints": self.enable_points,
            "enableGridX": self.enable_xgrid,
            "enableGridY": self.enable_ygrid}
        
        item_content_dict |= self.options | theme_dict | legends_dict

        return {"label": self.label,
                "key": self.key,
                "layout": self.layout,
                "item_type": self.__class__.__name__,
                "item_content": item_content_dict}
