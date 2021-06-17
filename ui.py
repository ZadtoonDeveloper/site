import streamlit as st
import math

st.title("This is host")
st.header("this is host yey")
st.write("Hello")

#name = st.text_input(label = "Name", max_chars = 10)
number1 = st.number_input(label = "number1", step = 1, min_value = -3*10**5, max_value = 3*10**5)
number2 = st.number_input(label = "number2", step = 1, min_value = -3*10**5, max_value = 3*10**5)
number3 = st.number_input(label = "number3", step = 1, min_value = -3*10**5, max_value = 3*10**5)

slider_ = st.slider(label = "slider", step = 1, min_value = -3*10**5, max_value = 3*10**5)
button_info = st.button(label = "Summa")
box = st.checkbox(label = "d a")
file = st.file_uploader(label = "file")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

radbutton = st.radio("What's you favourite movie genre", ("Comedy", "Drama", "Documentary"))
if radbutton == "Comedy":
    st.write("ok")

select = st.selectbox("How would you like to be contacted", ("Email", "Phone", "Mobile Phone"))
st.write("You selected: ", select)

multiselect = st.multiselect("Whta are you favourite colors", ["Green", "Yellow", "Red", "Blue"], ["Yellow", "Red"], help = "Help")
st.write("You selected: ", multiselect)
if file is not None:
    st.image(file)
if button_info:
    st.write(f"summa = {number1 / number2 + number3}")

