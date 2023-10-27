import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda S
l_s = 1    # Longitud de onda
a_s = 0.25 # Amplitud
b_s = 15   # Parámetro b
n_s = 100  # Número de términos en la serie
s1 = (a_s / (2 * b_s)) * (2 - b_s)
s2 = 0

# Generar la onda S
x_s = np.arange(0.01, 2.01, 0.01)
x_s = x_s - (l_s / 6)  # Ajustar la posición de x
onda1s = np.zeros(len(x_s))
for i in range(1, n_s + 1):
    harm3 = (((2 * b_s * (-a_s)) / (i * i * np.pi * np.pi) * (1 - np.cos((i * np.pi) / b_s)) * -np.cos((i * np.pi * x_s) / l_s)))
    s2 += harm3
    onda1s += harm3

ondas = -1 * (s1 + s2)

# Corregir el rango de x para la onda S
x_s = np.arange(0.01, 2.01, 0.01)

# Crear la gráfica para la onda S
fig_s, ax_s = plt.subplots(figsize=(8, 4))
ax_s.plot(x_s, ondas)
ax_s.grid(True)
ax_s.set_title("ONDA SINUSOIDAL S")
ax_s.set_xlabel("Tiempo (s)") 
ax_s.set_ylabel("Amplitud") 

# Configuración de la página Streamlit
st.set_page_config(
    page_title="Análisis de Señales Cardiovasculares",
    page_icon="❤️",
)

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra la onda sinusoidal S.")
    
    st.pyplot(fig_s, use_container_width=True)

if __name__ == "__main__":
    run()
