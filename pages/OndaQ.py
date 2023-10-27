import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular la serie de Fourier de la onda Q
def fourier_series_q(x_q, a_q, b_q, l_q, n_q):
    series_sum = 0
    q1 = (a_q / (2 * b_q)) * (2 - b_q)
    q2 = 0

    for i in range(1, n_q + 1):
        harm5 = (((2 * b_q * a_q) / (i * i * np.pi * np.pi) * (1 - np.cos((i * np.pi) / b_q))) * -np.cos((i * np.pi * x_q) / l_q))
        q2 += harm5
        series_sum += harm5

    ondaq = -1 * (q1 + q2)
    return ondaq

def run():
    st.write("# Análisis de Señales Cardiovasculares")

    st.markdown(
        """
## Onda Q
La onda Q en un electrocardiograma (ECG) es la primera onda del complejo QRS y representa la despolarización inicial de los ventrículos del corazón. Aunque es una onda pequeña, la presencia o ausencia de la onda Q, así como su forma y duración, son indicativos de diversas condiciones cardíacas. Algunas condiciones médicas relacionadas con la onda Q incluyen:
- **Infarto de miocardio:** La ausencia de onda Q en una derivación del ECG puede ser un indicio de un infarto agudo de miocardio.
- **Enfermedad cardíaca coronaria:** Cambios en la forma y duración de la onda Q pueden indicar problemas en las arterias coronarias.
        """
    )
    st.write("Esta aplicación genera y muestra la onda sinusoidal Q.")

    # Parámetros de la onda Q
    l_q = st.slider("Longitud de onda Q", min_value=0.1, max_value=2.0, value=1.0, step=0.01)
    a_q = st.slider("Amplitud Q", min_value=-0.1, max_value=0.1, value=-0.025, step=0.001)
    b_q = st.slider("Parámetro b Q", min_value=1, max_value=30, value=15, step=1)
    n_q = st.slider("Número de términos en la serie de Fourier", min_value=1, max_value=200, value=100)
    
    # Rango de tiempo
    x_q = np.arange(0.01, 2.01, 0.01) + (l_q / 6)

    ondaq = fourier_series_q(x_q, a_q, b_q, l_q, n_q)  # Calcular la onda Q

    # Crear la gráfica para la onda Q
    fig_q, ax_q = plt.subplots(figsize=(8, 4))
    ax_q.plot(x_q, ondaq)
    ax_q.grid(True)
    ax_q.set_title("ONDA SINUSOIDAL Q")
    ax_q.set_xlabel("Tiempo (s)") 
    ax_q.set_ylabel("Amplitud") 
    
    st.pyplot(fig_q, use_container_width=True)

if __name__ == "__main__":
    run()
