import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la serie de Fourier
def fourier_series(x, a, b, L, n_terms):
    series_sum = 0
    for n in range(1, n_terms + 1):
        term = (2 / np.pi) * ((np.sin(np.pi / (2 * b) * (b - 2 * n)) / (b - 2 * n)) + (np.sin(np.pi / (2 * b) * (b + 2 * n)) / (b + 2 * n)))
        term *= np.cos((n * np.pi / L) * x)
        series_sum += term
    return a * (1 / L) * series_sum

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.markdown(
        """
## Onda P
La onda P en un ECG representa la despolarización auricular, es decir, la contracción de las aurículas del corazón. Su importancia radica en la iniciación de la secuencia de eventos cardíacos. Algunas condiciones médicas relacionadas con la onda P incluyen:
- **Fibrilación auricular:** Una arritmia común en la que las aurículas laten de manera irregular y rápida.
       """
    )
    st.write("Esta aplicación genera y muestra la onda sinusoidal P.")
    amplitud = st.slider("Amplitud", min_value=0.01, max_value=1.0, value=0.25, step=0.01)
    longitud = st.slider("Longitud", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    b = st.slider("Parametro b", min_value=1, max_value=10, value=3)
    n_terms = st.slider("Número de términos en la serie de Fourier", min_value=1, max_value=100, value=10)

    # Rango de tiempo
    x = np.linspace(0, 2, 1000)
    x = x + (1 / 1.8)

    ondap = fourier_series(x, amplitud, b, longitud, n_terms)  # Calcular la onda P

    # Crear la gráfica
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(x, ondap)
    ax.grid(True)
    ax.set_title("ONDA SINUSOIDAL P")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Amplitud") 
    
    st.pyplot(fig, use_container_width=True)

if __name__ == "__main__":
    run()
