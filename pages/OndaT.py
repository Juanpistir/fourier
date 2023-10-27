import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la serie de Fourier de la onda T
def fourier_series_t(x_t, a_t, b_t, l_t, n_t):
    series_sum = 0
    t1 = 1 / l_t
    t2 = 0

    for i in range(1, n_t + 1):
        harm2 = (((np.sin((np.pi / (2 * b_t)) * (b_t - (2 * i))) / (b_t - (2 * i)) +
                  (np.sin((np.pi / (2 * b_t)) * (b_t + (2 * i))) / (b_t + (2 * i))) * (2 / np.pi)) *
                 np.cos((i * np.pi * x_t) / l_t)))
        t2 += harm2
        series_sum += harm2

    ondat1 = a_t * (t1 + t2)
    return ondat1

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.markdown(
        """
## Onda T
La onda T representa la repolarización ventricular, que es la recuperación de los ventrículos después de la contracción. Cambios en la onda T pueden ser indicativos de problemas cardíacos. Algunas condiciones médicas relacionadas con la onda T incluyen:
- **Síndrome de QT largo:** Un trastorno del ritmo cardíaco que puede llevar a arritmias potencialmente mortales.
- **Hipertrofia ventricular izquierda:** Un agrandamiento anormal del ventrículo izquierdo del corazón.

        """
    )
    st.write("Esta aplicación genera y muestra la onda sinusoidal T.")

    # Parámetros de la onda T
    l_t = st.slider("Longitud de onda T", min_value=0.1, max_value=2.0, value=1.0, step=0.01)
    a_t = st.slider("Amplitud T", min_value=0.1, max_value=1.0, value=0.35, step=0.01)
    b_t = st.slider("Parámetro b T", min_value=1, max_value=20, value=7, step=1)
    n_t = st.slider("Número de términos en la serie de Fourier", min_value=1, max_value=100, value=20)
    
    # Rango de tiempo
    x_t = np.arange(0.01, 2.01, 0.01)
    x_t = x_t - (1 / 1.8)  # Ajustar la posición de x

    ondat = fourier_series_t(x_t, a_t, b_t, l_t, n_t)  # Calcular la onda T

    # Crear la gráfica para la onda T
    fig_t, ax_t = plt.subplots(figsize=(8, 4))
    ax_t.plot(x_t, ondat)
    ax_t.grid(True)
    ax_t.set_title("ONDA SINUSOIDAL T")
    ax_t.set_xlabel("Tiempo (s)") 
    ax_t.set_ylabel("Amplitud") 
    
    st.pyplot(fig_t, use_container_width=True)

if __name__ == "__main__":
    run()
