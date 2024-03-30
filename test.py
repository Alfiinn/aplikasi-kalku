import streamlit as st

st.title('test running streamlit')
st.write("Hello **world**!")
st.write('Hello, *World!* :sunglasses:')
st.title('_alpin_is :blue[cool]')
st.title("_rai_is :blue[red]")
st.write('halo')
st.title('mataram is :red[red]')
st.title('mataram is :blue[blue]')
st.write('hooh')

st.header('Aplikasi Penjumlahan Bilangan Nomerik', divider='rainbow')

angka_pertama = st.number_input('Masukan Angka Pertama')
st.write('The first number is ', angka_pertama)

angka_kedua = st.number_input('Masukan Angka Kedua')
st.write('The Second number is ', angka_pertama)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua} = {operasi_matematika}")
