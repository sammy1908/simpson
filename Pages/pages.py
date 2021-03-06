from Method.method import simpson_method
import streamlit as st
import sympy as sp
from PIL import Image


def method_page():
    title = """
    <h1 class="title">Metodo de Simpson</h1>
    <style>
    .title{
        width:100%;
        text-align: center;
    }
    </style>
    """
    st.markdown(title, unsafe_allow_html=True)
    st.write(""" Para este programa se esta utilizando python, por lo tanto
                las potencias son equivalentes a ***, tambíen están los simbolos
                básicos de +,-,*,/ y  funciones como sen(), cos(), tan(), pi, sqrt()
                """)

    funcion = st.text_input("Inserta tu función")
    try:
        if funcion:
            f = sp.sympify(funcion)
            latex = sp.latex(f)
            st.latex(f""" Función  \ Ingresada: \ {latex}""")
    except:
        st.warning("Recuerda que debes añadir los simbolos de operación. Aparte utiliza x como variable")

    a = st.text_input("Limite inferior")
    b = st.text_input("Limite superior")
    n = st.text_input("Valor del intervalo n")

    btn = st.button("Calcular")

    if btn:
        try:
            result = simpson_method(f,sp.sympify(a),sp.sympify(b),sp.sympify(n))
            st.subheader(f"El resultado es: {round(result,3)}")
        except:
            st.warning("Recuerda añadir numeros en tu a b y n")


def pres_page():  
    title = """
    <div class="title">
        <h1>Universidad Tecnológica de Panamá</h1>
        <h2>Facultad de Ingeniería Industrial</h2>
    </div>
    <h2 class="materia">Licenciatura en Ingeniería Industrial</h2>
    <h2 class="materia">Métodos Numéricos</h2>
    <div class="integrantes">
        <h3>Ardila, Paola  8-972-1246</h3>
        <h3>Arjona, Itza 8-970-1372 </h3>
        <h3>González, Samantha E-8-174190</h3>
        <h3>Pinto, Mirelys 8-940-1920</h3>
        <h3>Buelvas, Yaneh 8-973-1181</h3>
    </div>

    <h3 class="profesor">Ing. Samuel Jiménez</h3>

    <h3>Semestre II 2021</h3>
    <style>
        h3,
        h2 {
        text-align: center;
        }
        .title {
        width: 100%;
        margin-bottom: 100px;
        text-align: center;
        }
        .integrantes {
        width: 100%;
        margin-bottom: 100px;
        text-align: center;
        }
        .materia {
        margin-bottom: 100px;
        }
        .profesor{
            margin-bottom:100px;
        }
    </style>
    """
    st.markdown(title, unsafe_allow_html=True)


def end_page():
    image = Image.open(r'saludo.png')
    title = """
    <h5 class="title">Muchas gracias por el tiempo dedicado profesor. Ha sido un placer para nosotras el contar con su apoyo, dedicación y compromiso, su labor es muy valiosa.</h5>
        <style>
        .title {
        width: 100%;
        text-align: center;
        }
    </style>
    """
    st.markdown(title , unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)
    with col2:
        st.image(image)

