import streamlit as st
import PyPDF2
from langchain.document_loaders import PyPDFLoader

file = st.file_uploader('upload', type='pdf')

if file is not None:
    temp_file = f'./{file.name}.pdf'
    with open(temp_file, 'wb') as f:
        f.write(file.getvalue())
        file_name = file.name
    
    loader = PyPDFLoader(temp_file)
    docs = loader.load_and_split()        
    st.write(loader.load())
    