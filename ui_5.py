import streamlit as st
import pandas as pd
import math
import time
st.set_page_config(page_title="Ex-stream-ly Cool App", page_icon="images/icon.ico.ico", layout="wide")

def vvivodP(ab, bc, ac):
    p = ab + bc + ac
    return p
def vvivodS(ab, bc, ac):
    p = vvivodP(ab, bc, ac) / 2
    return round((p * (p - ab) * (p - bc) * (p - ac))**(1/2), 2)
def show(n1, n2, n3):
    D = n2**2 - 4 * n3 * n1
    if D > 0:
        x1 = (n2 + math.sqrt(D)) / 2 * n1
        x2 = (n2 - math.sqrt(D)) / 2 * n1
        return(f"x1 = {round(x1, 2)}", f"x2 = {round(x2, 2)}")
    elif D == 0:
        x = -1 * n2 / 2 * n1
        return (f"x = {round(x, 2)}")
    else:
        return("Проблема: D < 0")
st.title("Треугольник основные величины")
st.image("images/triangle_abc.png")
col2, col4, col6 = st.beta_columns(3)
col2.write("AB")
col4.write("BC")
col6.write("AC")
ab = col2.number_input(label = " ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
bc = col4.number_input(label = "  ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
ac = col6.number_input(label = "   ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
col11, col12 = st.beta_columns(2)
result_show = col11.radio("Show", ("Периметр", "Площадь"))
button = col12.button(label = "Вывод")
if button:
    if ab + bc > ac and ab + ac > bc and ac + bc > ab:
        if result_show == "Периметр":
            st.success(f"P = {vvivodP(ab, bc, ac)}")
        elif result_show == "Площадь":
            st.success(f"S = {vvivodS(ab, bc, ac)}")

st.title("Квадратные уравнения")
st.header("Поиск корней квадртного уравнения:")
col1, col2, col3 = st.beta_columns(3)
col1.latex("x^2 +")
col2.latex(" x +")
col3.latex(" =0")
num1 = col1.number_input(label = "     ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
num2 = col2.number_input(label = "       ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
num3 = col3.number_input(label = "         ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
get_result = st.button(label = "получить корни")

if get_result:
    result = show(num1, num2, num3)
    if result == "Проблема: D < 0":
        st.warning(result)
    else:
        for x in result:
            st.success(x)

st.title("Графики")
st.write("X start")

x1 = st.slider(label = "x", step = 1, min_value = -3*10, max_value = 3*10)
st.write("X end")
x2 = st.slider(label = "x1", step = 1, min_value = -3*10, max_value = 3*10)
x_range = range(x1, x2)
y_range = [(x,x) for x in x_range]
y_range_2 = [(x,x**2) for x in x_range]
y_range_3 = [(x,x**3) for x in x_range]
show_graphic = st.button(label = "Show")
y_x = st.checkbox("y = x")
y_x2 = st.checkbox("y = x ^ 2")
y_x3 = st.checkbox("y = x ^ 3")

df = pd.DataFrame(y_range)
df2 = pd.DataFrame(y_range_2)
df3 = pd.DataFrame(y_range_3)

if show_graphic and y_x:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    st.line_chart(data=df)
    st.info("График y = x нарисован")
elif show_graphic and y_x2:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    st.line_chart(data=df2)
    st.info("График y = x^2 нарисован")
elif show_graphic and y_x3:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    st.line_chart(data=df3)
    st.info("График y = x^3 нарисован")
st.error("Some Text")
st.warning("Some Text")
st.exception(RuntimeError('This is an exception of type RuntimeError'))
st.info("Some Text")
st.success("Some Text")
with st.spinner('Wait for it...'):
    time.sleep(5)
    st.success('Done!')
video_file = open(r'videos/star.mp4', 'rb')
c1, c2 = st.beta_columns(2)
video_bytes = video_file.read()
c1.video(video_bytes)
c2.video(video_bytes)