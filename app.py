
import streamlit as st
from manager import Manager
import json


print("Starting...")

if "manager" not in st.session_state:
    print("Creating Manager...")
    st.session_state.manager = Manager()


st.session_state.manager.run()
