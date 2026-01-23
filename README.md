# Proyecto_Sprint7

ESTA APLICACION FUE CONSTRUIDA CON STEAMLIT Y FUNCIONA COMO UN TABLERO INTERACTIVO PARA LA EXPLORACION VISUAL DE UN CONJUNTO DE DATOS 

¿PARA QUE NOS SIRVE ESTE PROYECTO?

ESTO NOS SIRVE PARA TRANSFORMAR DATOS DE UN DATAFRAME EN INFORMACION VISUAL DONDE NOS PERMITA

*ENCONTRAR PATRONES
*VER Y ANALISAR RELACIONES 
*TOMAR DECISIONES

**LO QUE PODEMOS VER EN LA INTERFAZ**

Visualización de Distribución (Botón Histograma)
Al presionar el botón de "Construir histograma", la app procesa la columna odometer y genera un gráfico de barras que muestra cuántos vehículos hay en diferentes rangos de kilometraje. Es ideal para saber si los autos en venta son mayormente nuevos o muy usados.

Análisis de Correlación (Botón Gráfico de Dispersión)
Mediante el botón de "Construir gráfico de dispersión", la aplicación crea una comparativa entre dos variables (usualmente odometer vs price). Cada punto representa un vehículo, permitiendo visualizar si, a mayor kilometraje, el precio tiende a bajar de forma lineal.


**PASOS PARA ANTES DE CORRER EL CODIGO**

RECUERDA QUE ES IMPORTANTE ASEGURARTE DE TENER INSTALADAS LAS LIBRERIAS COMO LO SON python, steamlit, plotly_express y pandas

**Estos son los comandos de instalacion**

INSTALAR conda:
conda install anaconda::pandas

INSTALAR ploty_express:
conda install plotly::plotly_express

INSTALAR steamlit:
conda install conda-forge::streamlit

HABILITAR ploty_express con:
conda install -n myenv nbformat

**Ademas de iniciar conda con:**

conda activate vehicles_env

Y una vez tengas listas librerias en la terminal de bash deberas de ejecutar el codigo

steamlit run app.pp

**Liga del proyecto**
Aqui se encuentra la liga al proyecto en linea

https://proyecto-sprint7-iarh.onrender.com