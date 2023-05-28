import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# Configurar el estilo de la gráfica
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.style.use("seaborn")

# Crear el dashboard
st.title("Dashboard de Gasto de Agua")

# Crear una lista vacía para almacenar los datos
historial_gasto = []

gasto_actual_container = st.empty()

# Generar y mostrar los datos en tiempo real
chart = st.line_chart(historial_gasto)

# Simular la generación de datos en tiempo real
while True:
    # Generar dato de gasto de agua aleatorio
    gasto_actual = np.random.normal(loc=30, scale=10)  # Media: 30, Desviación estándar: 10
    gasto_actual = max(gasto_actual, 0)  # Asegurar que el gasto no sea negativo
    
    # Agregar el dato al historial
    historial_gasto.append(gasto_actual)
    
    # Actualizar la gráfica en tiempo real
    chart.add_rows([historial_gasto[-1]])
    
    # Mostrar el último dato de gasto de agua
    gasto_actual_container.subheader("Gasto de Agua Actual: {:.2f} l/s".format(gasto_actual))
    
    
    # Esperar 1 segundo antes de generar el siguiente dato
    time.sleep(1)
    
    #create a tab 