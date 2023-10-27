import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la serie de Fourier de la onda QRS
def fourier_series_r(x_qrs, a_qrs, b_qrs, l_qrs, n_qrs):
    series_sum = 0
    qrs1 = (a_qrs / (2 * b_qrs)) * (2 - b_qrs)
    qrs2 = 0

    for i in range(1, n_qrs + 1):
        harm = (((2 * b_qrs * a_qrs) / (i * i * np.pi * np.pi) * (1 - np.cos((i * np.pi) / b_qrs))) * np.cos((i * np.pi * x_qrs) / l_qrs))
        qrs2 += harm
        series_sum += harm

    ondaqrs = qrs1 + qrs2
    return ondaqrs

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.markdown(
        """
## Onda R
La onda R en un ECG representa la despolarización ventricular tardía, que es la fase final de la contracción de los ventrículos del corazón. La onda R es esencial para el bombeo efectivo de sangre hacia el sistema circulatorio. Algunas condiciones médicas relacionadas con la onda R incluyen:
- **Infarto de miocardio:** Un bloqueo súbito del flujo sanguíneo al corazón, que puede causar cambios en la onda R y el complejo QRS.
- **Bloqueo de rama:** Una interrupción en la conducción eléctrica en uno de los haces de fibras que llevan impulsos eléctricos a través de los ventrículos.

        """
    )

    st.write("Esta aplicación genera y muestra la onda sinusoidal R.")

    # Parámetros de la onda QRS
    l_qrs = st.slider("Longitud de onda R", min_value=0.1, max_value=2.0, value=1.0, step=0.01)
    a_qrs = st.slider("Amplitud R", min_value=0.1, max_value=2.0, value=1.0, step=0.01)
    b_qrs = st.slider("Parámetro b R", min_value=1, max_value=30, value=5, step=1)
    n_qrs = st.slider("Número de términos en la serie de Fourier", min_value=1, max_value=200, value=100)
    
    # Rango de tiempo
    x_qrs = np.arange(0.01, 2.01, 0.01)

    ondaqrs = fourier_series_r(x_qrs, a_qrs, b_qrs, l_qrs, n_qrs)  # Calcular la onda QRS

    # Crear la gráfica para la onda QRS
    fig_qrs, ax_qrs = plt.subplots(figsize=(8, 4))
    ax_qrs.plot(x_qrs, ondaqrs)
    ax_qrs.grid(True)
    ax_qrs.set_title("ONDA SINUSOIDAL R")
    ax_qrs.set_xlabel("Tiempo (s)") 
    ax_qrs.set_ylabel("Amplitud") 
    
    st.pyplot(fig_qrs, use_container_width=True)

if __name__ == "__main__":
    run()
