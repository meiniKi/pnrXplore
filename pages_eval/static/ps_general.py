
import streamlit as st
from streamlit_elements import elements, mui, html, dashboard
from streamlit_elements import nivo
from pathlib import Path
import json
import base64

class PSHelper:
    @staticmethod
    def get_iter_lbls(data):
        if data is None:
            st.error("No data index")
            return
        return data["iter_lbls"]
    
    @staticmethod
    def get_group_lbls(data):
        if data is None:
            st.error("No data index")
            return
        return data["group_lbls"]

    @staticmethod
    def image_path_to_base64(image_path):
        try:
            with open(image_path, "rb") as image_file:
                binary_data = image_file.read()
                base64_bytes = base64.b64encode(binary_data)
                base64_string = base64_bytes.decode('utf-8')
            return base64_string
        except Exception as e:
            st.error(f"Cannot load render {e}")
            return None



if st.session_state.get("psg", None) is None:
    st.session_state["pgs"] = True
    st.session_state["pgs_data_root"] = Path(st.session_state["uploaded_root"])/"static"
    with open(st.session_state["pgs_data_root"]/"index.json") as f:
        st.session_state["pgs_data"] = json.load(f)
    st.session_state["pgs_iter_lbls"] = PSHelper.get_iter_lbls(st.session_state["pgs_data"])
    st.session_state["pgs_group_lbls"] = PSHelper.get_group_lbls(st.session_state["pgs_data"])
    # Initial

st.title("Electrostatic Placer Eval")

st.select_slider(
    label="Iteration",
    key="pgs_sel_iter",
    options=st.session_state.get("pgs_iter_lbls", ["Error, Error"])
)

if st.session_state.get("pgs_sel_iter_val", "000") != st.session_state.get("pgs_sel_iter", None):
    st.session_state["pgs_sel_iter_val"] = str(st.session_state.get("pgs_sel_iter", None)).zfill(3)

st.select_slider(
    label="Group",
    key="pgs_sel_group",
    options=st.session_state.get("pgs_group_lbls", ["Error, Error"])
)

with elements("dashboard"):
    layout = [
        dashboard.Item("xoveriter", x=1, y=0, w=4, h=4, isDraggable=True, moved=False, isResizable=True),
        dashboard.Item("render", x=1, y=5, w=1, h=1, isResizable=True, isDraggable=True),
    ]

    with dashboard.Grid(layout):
        #mui.Paper("xoveriter", key="xoveriter")
        #mui.Paper("Render", key="render")

        image_style = {
            'width': '100%',
            'height': 'auto',
            'display': 'block',
        }

        with mui.Paper(key="render", type="outlined"):
            with mui.Typography:
                html.img(
                    src="data:image/png;base64,{}".format(
                        PSHelper.image_path_to_base64(st.session_state["pgs_data_root"]/"positions/pos_{}_{}.png".format(0, st.session_state["pgs_sel_iter_val"]))),
                    style=image_style)


        with elements("xoveriter"):
            DATA = [
                { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
                { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
                { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
                { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
                { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
            ]

            with mui.Box(sx={"height": 500}):
                nivo.Radar(
                    data=DATA,
                    keys=[ "chardonay", "carmenere", "syrah" ],
                    indexBy="taste",
                    valueFormat=">-.2f",
                    margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
                    borderColor={ "from": "color" },
                    gridLabelOffset=36,
                    dotSize=10,
                    dotColor={ "theme": "background" },
                    dotBorderWidth=2,
                    motionConfig="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ],
                    theme={
                        "background": "#FFFFFF",
                        "textColor": "#31333F",
                        "tooltip": {
                            "container": {
                                "background": "#FFFFFF",
                                "color": "#31333F",
                            }
                        }
                    }
                )