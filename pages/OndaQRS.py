import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda QRS
l_qrs = 1   # Longitud de onda
a_qrs = 1   # Amplitud
b_qrs = 5   # Parámetro b
n_qrs = 100  # Número de términos en la serie
qrs1 = (a_qrs / (2 * b_qrs)) * (2 - b_qrs)
qrs2 = 0

# Generar la onda QRS
x_qrs = np.arange(0.01, 2.01, 0.01)
onda1qrs = np.zeros(len(x_qrs))
for i in range(1, n_qrs + 1):
    harm = (((2 * b_qrs * a_qrs) / (i * i * np.pi * np.pi) * (1 - np.cos((i * np.pi) / b_qrs)) * np.cos((i * np.pi * x_qrs) / l_qrs)))
    qrs2 += harm
    onda1qrs += harm

ondaqrs = qrs1 + qrs2

# Corregir el rango de x para la onda QRS
x_qrs = np.arange(0.01, 2.01, 0.01)

# Crear la gráfica para la onda QRS
fig_qrs, ax_qrs = plt.subplots(figsize=(8, 4))
ax_qrs.plot(x_qrs, ondaqrs)
ax_qrs.grid(True)
ax_qrs.set_title("ONDA SINUSOIDAL QRS")
ax_qrs.set_xlabel("Tiempo (s)") 
ax_qrs.set_ylabel("Amplitud") 

# Configuración de la página Streamlit
st.set_page_config(
    page_title="Análisis de Señales Cardiovasculares",
    page_icon="❤️",
)

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra la onda sinusoidal QRS.")
    
    st.pyplot(fig_qrs, use_container_width=True)
    
if __name__ == "__main__":
    run()
