
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
    def __load_index():
        if (p := st.session_state.get("manger_uploaded_root", None)) is not None:
            with open(Path(p)/"index.json") as f:
                st.session_state.manger_pages_dict = json.load(f)


    def generate(self) -> List:
        self.__load_index()
        pages = [st.Page("page_upload.py")]

        if st.session_state.get("manger_uploaded_root", None) is not None:
            for p in st.session_state.get("manger_pages_dict", []):
                print("generate: append: {}".format(p["key"]))
                # Cannot pass parameters, thus, use some globale storage
                st.session_state.page_generate_key = p["key"]
                pages.append(st.Page(
                    page=PageEvalGenerator.generate,
                    title=p["title"],
                    url_path=p["key"]
                ))
        st.session_state.pages_generated = pages


    def reset(self):
        st.session_state.manger_uploaded_root = None
        # For debugging
        if st.session_state.get("debug", None) is not None:
            st.session_state.manger_uploaded_root = Path("archives/run/").absolute()
            self.__load_page_keys()



    def run(self):
        pg = None
        #if st.session_state.get("manger_pages_dict", None) is None:
        self.generate()
        pg = st.navigation(st.session_state.pages_generated)
        st.session_state.page_generate_key = pg.url_path
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

