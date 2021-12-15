import streamlit as st
from PIL import Image

from Pages.pages import method_page,pres_page,end_page

image = Image.open(r'Logos.png')
st.image(image)

page = "Presentación"
page = st.sidebar.selectbox("Pagina a elegir",["Presentación", "Calcular","Despedida"])


if page == "Presentación":
    pres_page()

if page == "Calcular":
    method_page()

if page == "Despedida":
    end_page()