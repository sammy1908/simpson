import streamlit as st
from PIL import Image

from Method.method import method_page,pres_page

image = Image.open(r'C:\Users\Juan Riquelme\Documents\TRABAJOS\CODING\Proyectos\Simpson\Logos.png')
st.image(image)

page = "Presentación"
page = st.sidebar.selectbox("Pagina a elegir",["Presentación", "Calcular"])


if page == "Presentación":
    pres_page()

if page == "Calcular":
    method_page()