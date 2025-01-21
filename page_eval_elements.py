
from typing import Dict
import streamlit as st

class PageEvalElements:
    @staticmethod
    def PnrXploreControlSliderSelect(ele: Dict):
        st.select_slider(
            label=ele["label"],
            key=ele["key"],
            options=ele["options"])


