import streamlit as st
import math

def show(n1, n2, n3):
    D = n2**2 - 4 * n3 * n1
    if D > 0:
        x1 = (n2 + math.sqrt(D)) / 2 * n1
        x2 = (n2 - math.sqrt(D)) / 2 * n1
        return(f"x1 = {x1} \n x2 = {x2}")
    elif D == 0:
        x = -1 * n2 / 2 * n1
        return (f"x = {x}")
    else:
        return("Проблема: D < 0")
st.title("Квадратные уравнения")
st.header("Поиск корней квадртного уравнения:")
col1, col2, col3 = st.beta_columns(3)
col1.latex("x^2 +")
col2.latex(" x +")
col3.latex(" =0")
num1 = col1.number_input(label = " ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
num2 = col2.number_input(label = "  ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)
num3 = col3.number_input(label = "   ", step = 1, min_value = -3*10**5, max_value = 3*10**5, value = 0)


get_result = st.button(label = "получить корни")
if get_result:
    st.subheader(show(num1, num2, num3))
