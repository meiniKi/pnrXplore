

import streamlit as st

class Manager:
    def __init__(self) -> None:
        self.active_pages = list()
        st.session_state["data_uploaded"] = None

    def reset(self):
        self.active_pages = list()

    def clear_pages(self):
        self.pages = list()
        #self.pages.append(PageDefault("p_view_default", "Upload your Data"))

    def add_page(self, key, title, *args, **kwargs) -> None:
        pass

    def run(self):
        if not "monitors" in st.session_state:
            st.session_state.monitors = None

        if len(self.active_pages) > 0:
            pg = st.navigation(self.active_pages)
        else:
            #pg = st.navigation([st.Page("pages_eval/upload.py")])
            pg = st.navigation([st.Page("pages_eval/static/ps_general.py")])

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
