import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la serie de Fourier
def fourier_series_u(x, a, b, L, n_terms):
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
## Onda U
La onda U es una pequeña onda que sigue a la onda T. Aunque su función exacta no se comprende completamente, se asocia con la repolarización tardía y puede variar en tamaño. Cambios en la onda U pueden estar relacionados con:
- **Hipopotasemia:** Niveles bajos de potasio en la sangre, que pueden causar alteraciones en la onda U.


        """
    )
    st.write("Esta aplicación genera y muestra la onda sinusoidal U.")

    # Parámetros de la onda U
    l_u = st.slider("Longitud de onda U", min_value=0.1, max_value=2.0, value=1.0, step=0.01)
    a_u = st.slider("Amplitud U", min_value=0.01, max_value=0.1, value=0.03, step=0.01)
    b_u = st.slider("Parámetro b U", min_value=1, max_value=30, value=21, step=1)
    n_u = st.slider("Número de términos en la serie de Fourier", min_value=1, max_value=200, value=100)
    
    # Rango de tiempo
    x_u = np.arange(0.01, 2.01, 0.01)
    x_u = x_u - (1 / 1.1)  # Ajustar la posición de x

    ondau = fourier_series_u(x_u, a_u, b_u, l_u, n_u)  # Calcular la onda U

    # Crear la gráfica para la onda U
    fig_u, ax_u = plt.subplots(figsize=(8, 4))
    ax_u.plot(x_u, ondau)
    ax_u.grid(True)
    ax_u.set_title("ONDA SINUSOIDAL U")
    ax_u.set_xlabel("Tiempo (s)") 
    ax_u.set_ylabel("Amplitud") 
    
    st.pyplot(fig_u, use_container_width=True)

if __name__ == "__main__":
    run()
