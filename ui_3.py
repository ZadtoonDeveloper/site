import streamlit as st
import math

st.title("Container")
container = st.beta_container()
container.header("Header 1")
container.radio("radio", ("1", "2", "3"))
container.checkbox("1")
container.checkbox("2")
container.checkbox("3")
container.checkbox(label = "d a")
container.slider(label = "slider", step = 1, min_value = 0, max_value = 10)

container2 = st.beta_container()
container2.header("Header 2")
container2.multiselect("Multiselect", ["apple", "orange", "beanes", "carrot"])
file = container2.file_uploader(label = "file here")
if file is not None:
    st.image(file)