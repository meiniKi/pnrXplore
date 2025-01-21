
import streamlit as st
from pathlib import Path
import zipfile
import io

def process_uploaded_archive(zip_file, storage_dict):
    zip_buffer = io.BytesIO()
    zip_buffer.write(zip_file.read())
    zip_buffer.seek(0)

    with zipfile.ZipFile(zip_buffer, 'r') as z:
        for filename in z.namelist():
            with z.open(filename) as f:
                extracted_content = io.BytesIO(f.read())
                storage_dict[filename] = extracted_content


st.title("Upload or Select nextpnr Data")

uploaded_archive = st.file_uploader(
    "Upload an archvie",
    accept_multiple_files=False
)

if uploaded_archive is not None:
    process_uploaded_archive(uploaded_archive, st.session_state["data_uploaded"])


st.selectbox(
    label="Select from Default Folder",
    options = list({str(file.stem) for file in Path("./archives").rglob('*.zip') if file.is_file()}),
)

if st.button("Start"):
    pass

