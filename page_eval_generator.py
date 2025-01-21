
from pathlib import PosixPath
from typing import Dict, List
import streamlit as st
import json
from page_eval_elements import PageEvalElements

class PageEvalGenerator:

    @staticmethod
    def __load_page_data(data_key: str, path: PosixPath):
        with open(path) as f:
            st.session_state.data_key = json.load(f)

    @staticmethod
    def __generate_controls(elements: List, page_root: PosixPath):
        for ele in elements:
            if ele["type"] == "PnrXploreControlSliderSelect":
                PageEvalElements.PnrXploreControlSliderSelect(ele)

    @staticmethod
    def generate():
        page_key = st.session_state.page_key
        page_root = st.session_state.manger_uploaded_root/page_key
        data_key = f"{page_key}_data"
        if not page_key in st.session_state:
            st.session_state.page_key = True
            PageEvalGenerator.__load_page_data(data_key, page_root/"data.json")

        data = st.session_state.data_key
        st.title(data["title"])

        elements_dict = data["elements"]
        if "controls" in elements_dict:
            PageEvalGenerator.__generate_controls(elements_dict["controls"], page_root)
