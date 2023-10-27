import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros de la onda Q
l_q = 1   # Longitud de onda
a_q = -0.025 # Amplitud
b_q = 15    # Parámetro b
n_q = 100  # Número de términos en la serie
q1 = (a_q / (2 * b_q)) * (2 - b_q)
q2 = 0

# Generar la onda Q
x_q = np.arange(0.01, 2.01, 0.01)
x_q = x_q + (l_q / 6)

onda1q = np.zeros(len(x_q))
for i in range(1, n_q + 1):
    harm5 = (((2 * b_q * a_q) / (i * i * np.pi * np.pi) * (1 - np.cos((i * np.pi) / b_q))) * -np.cos((i * np.pi * x_q) / l_q))
    q2 += harm5
    onda1q += harm5

ondaq = -1 * (q1 + q2)

# Corregir el rango de x para la onda Q
x_q = np.arange(0.01, 2.01, 0.01) + (l_q / 6)

# Crear la gráfica para la onda Q
fig_q, ax_q = plt.subplots(figsize=(8, 4))
ax_q.plot(x_q, ondaq)
ax_q.grid(True)
ax_q.set_title("ONDA SINUSOIDAL Q")
ax_q.set_xlabel("Tiempo (s)") 
ax_q.set_ylabel("Amplitud") 

# Configuración de la página Streamlit
st.set_page_config(
    page_title="Análisis de Señales Cardiovasculares",
    page_icon="❤️",
)

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra la onda sinusoidal Q.")
    
    st.pyplot(fig_q, use_container_width=True)


if __name__ == "__main__":
    run()
