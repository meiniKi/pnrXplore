
import streamlit as st
from manager import Manager


import json
st.session_state["uploaded_root"] = "/home/user/Documents/repos/pnrXplore/archives/run"

with open("/home/user/Documents/repos/pnrXplore/archives/run/index.json") as f:
    st.session_state["uploaded_index"] = json.load(f)


app = Manager()
app.run()
