# Simulador de Colas en Python con Tkinter

Este es un simulador de colas en Python que utiliza la biblioteca Tkinter para la interfaz gráfica. La aplicación permite simular colas mediante la introducción de datos de entrada proporcionados por el usuario. Los datos incluyen la media tasa de llegada (distribución de Poisson), la media tasa de servicio (distribución normal), la desviación estándar del servicio, el total de clientes y el número de iteraciones (cantidad de colas simuladas).

## Requisitos

- Tener instalado Python en su sistema
- Instalar las dependencias necesarias ejecutando el siguiente comando: `pip install -r requirements.txt`

## Uso

Ejecute la aplicación ejecutando el archivo `Win1.py` con el siguiente comando `python Win1.py`

La interfaz gráfica le permitirá ingresar los parámetros necesarios y realizar la simulación de colas. A continuación se describen las funcionalidades clave:

### Simulación de Colas

1. **Media Tasa de Llegada:** Introduzca la media tasa de llegada para la distribución de Poisson.
2. **Media Tasa de Servicio:** Introduzca la media tasa de servicio para la distribución normal.
3. **Desviación Estándar del Servicio:** Introduzca la desviación estándar del servicio para la distribución normal.
4. **Total de Clientes:** Especifique el número total de clientes.
5. **Número de Iteraciones:** Indique la cantidad de colas que se simularán.

![image](https://github.com/JohanCortes/Queues/assets/37446976/0ae2cce7-08e6-413b-a4f2-6dd93533d7d7)

### Visualización de Resultados

1. **Gráficas:** Visualice los resultados de cada cola simulada gráficamente.
2. **Exportar a CSV:** Exporte los resultados de la cola seleccionada a un archivo CSV.
3. **Estadísticas Teóricas:** Genere estadísticas teóricas basadas en los parámetros ingresados.

![image](https://github.com/JohanCortes/Queues/assets/37446976/256a99c2-2152-40e1-a856-1ac03196e9f1)

### Análisis Global

1. **Resultados de Todas las Colas:** Seleccione los resultados de los tiempos de todas las colas para análisis global.
2. **Estadísticas Globales:** Encuentre el máximo, mínimo, media, desviación estándar, intervalos de confianza, etc.
3. **Gráficas Globales:** Visualice los resultados globales mediante gráficas.

![image](https://github.com/JohanCortes/Queues/assets/37446976/29d7c2d1-7f00-4c11-b1b5-d9da36760e12)

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles.
