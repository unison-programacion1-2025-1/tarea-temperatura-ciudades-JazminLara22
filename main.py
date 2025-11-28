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
    return kelvin - 273.15
    
# TODO: Copiar el DataFrame original y nombralo df_celsius
df_celsius = df.copy()

# TODO: Convertir las temperaturas de cada ciudad de Kelvin a Celsius usando la funcion creada
ciudades = ['San Diego', 'Phoenix', 'Toronto']

for ciudad in ciudades:
    if ciudad in df_celsius.columns:
        df_celsius[ciudad] = df_celsius[ciudad].apply(kelvin_to_celsius)
    else:
        print(f"No se encontró la columna {ciudad}")
        
# Analisis

# TODO: temperaturas y fechas en Phoenix
if 'Phoenix' in df_celsius.columns:
    
    # Mínima
    idx_min = df_celsius['Phoenix'].idxmin()
    temp_min = df_celsius['Phoenix'].min()
    
    # Máxima
    idx_max = df_celsius['Phoenix'].idxmax()
    temp_max = df_celsius['Phoenix'].max()
    
    # Promedio
    temp_mean = df_celsius['Phoenix'].mean()
    
    # Convertir fechas a string
    fecha_min_str = idx_min.strftime('%Y-%m-%d %H:%M:%S')
    fecha_max_str = idx_max.strftime('%Y-%m-%d %H:%M:%S')
    
    # Impresiones solicitadas
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



