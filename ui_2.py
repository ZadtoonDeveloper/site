import streamlit as st
import math



container = st.beta_container()

answer = st.radio("Есть ли жизнь на Марсе?", ("Да", "Нет", "Моя бабушка там живет"))
answer2 = st.multiselect("Выберите два ответа", ["Один ответ", "Второй ответ", "Третий ответ"])
st.write(answer2)
answer3 = container.number_input("Сколько будет 2 + 2?", help = "Введи ответ самолично, идиот")
if answer == "Нет" and answer2[0] == "Один ответ" and answer2[1] == "Второй ответ":
    st.write("Поздравляю, вы круты!")
    st.balloons()
container2 = st.beta_container()
container2.title("Вопросы")