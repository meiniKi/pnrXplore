
from pathlib import PosixPath
from streamlit_elements import elements, mui, html, dashboard, nivo
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
        cols = st.columns(len(elements))
        for i, ele in enumerate(elements):
            with cols[i]:
                if ele["type"] == "PnrXploreControlSliderSelect":
                    PageEvalElements.PnrXploreControlSliderSelect(ele)
            # TODO: Add further control components here
        
    def __generate_dashboard(items: List, page_root: PosixPath):
        layout = [dashboard.Item(i=i["key"], **i["layout"]) for i in items]
        with elements("dashboard"):
            with dashboard.Grid(layout):
                for i in items:
                    if i["item_type"] == "PnrXploreDashLine":
                       PageEvalElements.PnrXploreDashLine(i)
                    if i["item_type"] == "PnrXploreDashStateImage":
                       PageEvalElements.PnrXploreDashStateImage(i, page_root)


    @staticmethod
    def generate():
        page_key = st.session_state.page_key
        page_root = st.session_state.manger_uploaded_root/page_key
        data_key = f"{page_key}_data"
        if not page_key in st.session_state:
            st.session_state.page_key = True
            PageEvalGenerator.__load_page_data(data_key, page_root/"data.json")

        data = st.session_state.data_key

        st.markdown("""<style> .block-container {
                        padding-top:    0.8rem;
                        padding-bottom: 0rem;
                        padding-left:   5rem;
                        padding-right:  5rem;
                    } </style>""", unsafe_allow_html=True)
        st.title(data["title"])

        elements_dict = data["elements"]
        if "controls" in elements_dict:
            PageEvalGenerator.__generate_controls(elements_dict["controls"], page_root)
        if "dashboard" in elements_dict:
            PageEvalGenerator.__generate_dashboard(elements_dict["dashboard"], page_root)