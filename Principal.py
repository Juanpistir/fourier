import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

import neurokit2 as nk  # Load the package

simulated_ecg = nk.ecg_simulate(duration=3, sampling_rate=200, heart_rate=80)

fig = nk.signal_plot(simulated_ecg, sampling_rate=200)  # Visualize the signal


# Configuración de la página Streamlit
st.set_page_config(
    page_title="Análisis de Señales Cardiovasculares",
    page_icon="❤️",
)

def run():
    st.write("# Análisis de Señales Cardiovasculares")
    st.write("Esta aplicación genera y muestra una simulación de una señal ECG natural")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot(fig)
    




if __name__ == "__main__":
    run()
