import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Date' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# TODO: Crear funcion para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    try:
        return kelvin - 273.15
    except exeption:
        return float('nan')
    

# TODO: Copiar el DataFrame original y nombralo df_celsius
df_celsius = df.copy()
# TODO: Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la funcion creada
ciudades= ['San Diego', 'Phoenix', 'Toronto']
for ciudades in ciudades:
    if ciudad in df_celcius.columns:
        df_celsius[ciudad] = df_celcius[ciudad[.apply(kelvin_to_celcius)
    else:
        print("En la columna ciudad no se encontro la columna ciudad")
# Analisis

# TODO: Imprime que día y hora se registró la temperatura mínima en Phoenix con el siguiente mensaje: "El día con la temperatura mínima en Phoenix fue: {fecha}"
# TODO: Imprime la temperatura mínima en Phoenix con el siguiente mensaje: "La temperatura mínima registrada en Phoenix fue de: ", temperatura, " °C""

# TODO: Imprime que día y hora se registró la temperatura máxima en Phoenix con el siguiente mensaje: "El día con la temperatura máxima en Phoenix fue: {fecha}"
# TODO: Imprime la temperatura máxima en Phoenix con el siguiente mensaje: "La temperatura máxima registrada en Phoenix fue de: ", temperatura, " °C""

# TODO: Imprime la temperatura promedio en Phoenix durante el año 2016 con el siguiente mensaje: "La temperatura promedio durante 2016 en Phoenix fue de: ", temperatura, " °C""
if 'Phoenix' in df_celsius.columns:
        idx_min = df_celcius['phoenix'].idxmin()
        temp_min = df_celcius['Phoenix'].min()
        idx_max = df_celcius['Phoenix'].idxmax()
        tem_maz = df_calcius['Phoenix'].max
        tem_mean = df_celsius['phoenix'].mean()
        fecha_min_str = idx_min.strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(idx_min) else 'N/A'
        fecha_max_str = idx_max.strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(idx_max) else 'N/A'

    print(f"El día con la temperatura mínima en Phoenix fue: {fecha_min_str}")
    print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min:.2f} °C")

    print(f"El día con la temperatura máxima en Phoenix fue: {fecha_max_str}")
    print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max:.2f} °C")

    print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_mean:.2f} °C")
else:
    print("La columna 'Phoenix' no se encuentra en el DataFrame transformado.")
# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
plt.scatter(df_celsius.index, df_celsius['Phoenix'], label='Phoenix')
plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV
df_celsius.to_csv("temperatura_celsius.csv")


