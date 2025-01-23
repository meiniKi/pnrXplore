
import json
from typing import List
from pathlib import Path, PosixPath
import streamlit as st
from page_eval_generator import PageEvalGenerator

class Manager:
    def __init__(self) -> None:
        self.reset()
        st.set_page_config(
            page_title="pnrXplore",
            layout="wide",
            initial_sidebar_state="collapsed"
        )

    @staticmethod
    def __load_page_keys():
        if (p := st.session_state.get("manger_uploaded_root", None)) is not None:
            with open(Path(p)/"index.json") as f:
                st.session_state.manger_pages_keys = json.load(f)

    def reset(self):
        st.session_state.manger_uploaded_root = None
        # For debugging
        if st.session_state.get("debug", None) is not None:
            st.session_state.manger_uploaded_root = Path("archives/run/").absolute()
            self.__load_page_keys()

    def generate(self) -> List:
        pages = []
        for pk in st.session_state.get("manger_pages_keys", []):
            # Cannot pass parameters, thus, use some globale storage
            st.session_state.page_key = pk
            pages.append(st.Page(
                page=PageEvalGenerator.generate,
                title="TODO: title"
            ))
        return pages

    def run(self):
        pg = None

        pg = st.navigation([st.Page("page_debug.py")])
        pg.run()
        return

        if st.session_state.get("manger_pages_keys", None) is None:
            self.__load_page_keys()
        if st.session_state.get("manger_uploaded_root", None) is None:
            pg = st.navigation([st.Page("page_upload.py")])
        else:
            p = self.generate()
            pg = st.navigation(p)
        pg.run()

        #logout_page = st.Page(self.reset, title="Log out", icon=":material/logout:")
        
        #st.sidebar.title("Dashboard title")
        #st.sidebar.write("### Choose your dashboard")
        #page = st.sidebar.selectbox(
        #    'Dashboard:', 
        #    self.pages, 
        #    format_func=lambda page: page['title']
        #)

        # run the app function 
        #page['function'](*page["args"], **page["kwargs"])
        #for p 

