import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda T
l_t = 1    # Longitud de onda
a_t = 0.35 # Amplitud
b_t = 7    # Parámetro b
n_t = 20   # Número de términos en la serie
t1 = 1 / l_t
t2 = 0

# Generar la onda T
x_t = np.arange(0.01, 2.01, 0.01)
x_t = x_t - (1 / 1.8)  # Ajustar la posición de x
ondat1 = np.zeros(len(x_t))
for i in range(1, n_t + 1):
    harm2 = (((np.sin((np.pi / (2 * b_t)) * (b_t - (2 * i))) / (b_t - (2 * i)) +
              (np.sin((np.pi / (2 * b_t)) * (b_t + (2 * i))) / (b_t + (2 * i))) * (2 / np.pi)) *
             np.cos((i * np.pi * x_t) / l_t)))
    t2 += harm2
    ondat1 += harm2

ondat = a_t * (t1 + t2)

# Corregir el rango de x para la onda T
x_t = np.arange(0.01, 2.01, 0.01)

# Crear la gráfica para la onda T
fig_t, ax_t = plt.subplots(figsize=(8, 4))
ax_t.plot(x_t, ondat)
ax_t.grid(True)
ax_t.set_title("ONDA SINUSOIDAL T")
ax_t.set_xlabel("Tiempo (s)") 
ax_t.set_ylabel("Amplitud") 

# Configuración de la página Streamlit
st.set_page_config(
    page_title="Análisis de Señales Cardiovasculares",
    page_icon="❤️",
)

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra la onda sinusoidal T.")
    
    st.pyplot(fig_t, use_container_width=True)

if __name__ == "__main__":
    run()
