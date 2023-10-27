import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros
l = 1.0  # Longitud de onda
a = 0.25  # Amplitud
b = 3
n = 100

# Rango de tiempo
x = np.linspace(0, 2, 1000)
x = x + (1 / 1.8)

# Función para calcular la onda P
def calculate_waveform(x, l, a, b, n):
    ondap = np.zeros(len(x))
    for i in range(1, n + 1):
        harm = (((np.sin((np.pi / (2 * b)) * (b - (2 * i))) / (b - (2 * i))) +
                 (np.sin((np.pi / (2 * b)) * (-b + (2 * i))) / (b + (2 * i))) * (2 / np.pi)) *
                np.cos((i * np.pi * x) / l))
        ondap += harm

    ondap = a * ondap
    return ondap

# Calcular la onda P
ondap = calculate_waveform(x, l, a, b, n)

# Crear la gráfica
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(x, ondap)
ax.grid(True)
ax.set_title("ONDA SINUSOIDAL P")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Amplitud") 

# Configuración de la página Streamlit
st.set_page_config(
    page_title="Análisis de Señales Cardiovasculares",
    page_icon="❤️",
)

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra la onda sinusoidal P.")
    
    st.pyplot(fig, use_container_width=True)

if __name__ == "__main__":
    run()
