import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# car_data = pd.read_csv('C:/Users/edder/anaconda3/envs/Proyecto7/Proyecto_Sprint7/vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# --- AQUI PONGO EL GRAFICO DE DISPERCION---
scatter_button = st.button(
    'Construir gráfico de dispersión')  # crear el nuevo boton de dispersion vea

if scatter_button:
    # escribir un mensaje xd
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')

    # crear un grafico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")

    # mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)
