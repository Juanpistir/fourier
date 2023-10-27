import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda U
l_u = 1    # Longitud de onda
a_u = 0.03  # Amplitud
b_u = 21    # Parámetro b
n_u = 100   # Número de términos en la serie
u1 = 1 / l_u
u2 = 0

# Generar la onda U
x_u = np.arange(0.01, 2.01, 0.01)
x_u = x_u - (1 / 1.1)  # Ajustar la posición de x
ondau1 = np.zeros(len(x_u))
for i in range(1, n_u + 1):
    harm4 = (((np.sin((np.pi / (2 * b_u)) * (b_u - (2 * i))) / (b_u - (2 * i)) +
              (np.sin((np.pi / (2 * b_u)) * (b_u + (2 * i))) / (b_u + (2 * i))) * (2 / np.pi)) *
             np.cos((i * np.pi * x_u) / l_u)))
    u2 += harm4
    ondau1 += harm4

ondau = a_u * (u1 + u2)

# Corregir el rango de x para la onda U
x_u = np.arange(0.01, 2.01, 0.01)

# Crear la gráfica para la onda U
fig_u, ax_u = plt.subplots(figsize=(8, 4))
ax_u.plot(x_u, ondau)
ax_u.grid(True)
ax_u.set_title("ONDA SINUSOIDAL U")
ax_u.set_xlabel("Tiempo (s)") 
ax_u.set_ylabel("Amplitud") 

# Configuración de la página Streamlit
st.set_page_config(
    page_title="Análisis de Señales Cardiovasculares",
    page_icon="❤️",
)

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra la onda sinusoidal U.")
    
    st.pyplot(fig_u, use_container_width=True)

if __name__ == "__main__":
    run()
