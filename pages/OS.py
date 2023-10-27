import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la serie de Fourier de la onda S
def fourier_series_s(x_s, a_s, b_s, l_s, n_s):
    series_sum = 0
    s1 = (a_s / (2 * b_s)) * (2 - b_s)
    s2 = 0

    for i in range(1, n_s + 1):
        harm3 = (((2 * b_s * (-a_s)) / (i * i * np.pi * np.pi) * (1 - np.cos((i * np.pi) / b_s))) * -np.cos((i * np.pi * x_s) / l_s))
        s2 += harm3
        series_sum += harm3

    ondas = -1 * (s1 + s2)
    return ondas

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra la onda sinusoidal S.")

    # Parámetros de la onda S
    l_s = st.slider("Longitud de onda S", min_value=0.1, max_value=2.0, value=1.0, step=0.01)
    a_s = st.slider("Amplitud S", min_value=0.01, max_value=0.5, value=0.25, step=0.01)
    b_s = st.slider("Parámetro b S", min_value=1, max_value=30, value=15, step=1)
    n_s = st.slider("Número de términos en la serie de Fourier", min_value=1, max_value=200, value=100)
    
    # Rango de tiempo
    x_s = np.arange(0.01, 2.01, 0.01)
    x_s = x_s - (l_s / 6)  # Ajustar la posición de x

    ondas = fourier_series_s(x_s, a_s, b_s, l_s, n_s)  # Calcular la onda S

    # Crear la gráfica para la onda S
    fig_s, ax_s = plt.subplots(figsize=(8, 4))
    ax_s.plot(x_s, ondas)
    ax_s.grid(True)
    ax_s.set_title("ONDA SINUSOIDAL S")
    ax_s.set_xlabel("Tiempo (s)") 
    ax_s.set_ylabel("Amplitud") 
    
    st.pyplot(fig_s, use_container_width=True)

if __name__ == "__main__":
    run()
