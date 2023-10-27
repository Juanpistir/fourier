import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from st_pages import Page, Section, add_page_title, show_pages

add_page_title()

show_pages([
    Page("Hello.py", "Bienvenidos", "✔️"),
    Section("Ondas", icon="🌫️"),
    Page("pages/OP.py", "Ver Onda P", "🟧"),
    Page("pages/OQ.py", "Ver Onda Q", "🟨"),
    Page("pages/OR.py", "Ver Onda R", "🟧"),
    Page("pages/OS.py", "Ver Onda S", "🟦"),
    Page("pages/OT.py", "Ver Onda T", "🟫"),
    Page("pages/OU.py", "Ver Onda U", "⬜"),
])


def run():
    st.markdown(
        """
# Análisis de Señales Cardiovasculares con Series de Fourier ⚡

¡Bienvenido a nuestra aplicación de análisis de señales cardiovasculares! Esta herramienta utiliza series de Fourier para descomponer y visualizar las ondas cardíacas P, Q, R, S, T y U. El procesamiento digital de señales cardiovasculares desempeña un papel crucial en la detección temprana y el diagnóstico de trastornos cardíacos.
 
"""
    )

    st.image("images/ondasCardiacas.png")

    st.markdown(
    """
## Importancia de las Series de Fourier en el Procesamiento de Señales 🌌

Las series de Fourier son una herramienta fundamental en el análisis de señales periódicas, como las ondas cardíacas. Permite descomponer estas señales en sus componentes fundamentales, lo que facilita la identificación de patrones anómalos y la evaluación de la salud cardíaca. Nuestra aplicación utiliza estas técnicas para desglosar las ondas del ECG y proporcionar información valiosa sobre la función cardíaca.

    """
)

    
    st.image("images/SerieFourier.png")

    st.markdown(
    """
## Cómo Utilizar la Aplicación ⬇️

1. Selecciona la onda que deseas analizar: P, Q, R, S, T o U.
2. Ajusta los parámetros, como la amplitud, la longitud y el número de términos en la serie de Fourier, utilizando los controles deslizantes interactivos.
3. Observa la onda descompuesta y su importancia en la detección de trastornos cardíacos.
4. Explora cada onda por separado y aprende sobre las enfermedades relacionadas con cada una.

Esta aplicación es una herramienta educativa y de análisis que puede ser útil para estudiantes, profesionales de la salud y entusiastas de la cardiología. ¡Esperamos que disfrutes explorando las señales cardiovasculares y aprendiendo sobre su importancia en el diagnóstico de enfermedades cardíacas!🧐
     
Finalmente, esta aplicación fue desarrollada con dedicación y esfuerzo por Juan Pablo Hurtado Arce. ¡Espero que la disfrutes!. 😊".  
    """
)



if __name__ == "__main__":
    run()
