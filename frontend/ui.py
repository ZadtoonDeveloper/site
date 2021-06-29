import streamlit as st
import requests

base_url = "http://127.0.0.1:8000"
get_time = st.button(label = "get a time")

input = st.text_input(label = "name", value = "")
get_personal = st.button(label = "get a persona")

input1 = st.text_input(label = "a =", value = " ")
input2 = st.text_input(label = "b =", value = "  ")
get_triangle = st.button(label = "area-triangle-90")

#'/personal'
if get_time:
    st.write((requests.get(base_url + "/datetime")).text)
if get_personal:
    st.write((requests.post(base_url + "/personal", json = {"name" : input})).text)
if get_triangle:
    st.write((requests.post(base_url + '/area-triangle-90', json = {"a" : int(input1), "b" : int(input2)})).text)