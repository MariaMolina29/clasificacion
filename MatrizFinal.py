import pandas as pd

# Leer los archivos CSV
matriz_manzanas = pd.read_csv("Matriz_Manzanas.csv")
matriz_blueberries = pd.read_csv("Matriz_Blueberries.csv")

# Concatenar los DataFrames
matriz_concatenada = pd.concat([matriz_manzanas, matriz_blueberries], ignore_index=True)

# Agregar la nueva columna basada en la primera columna ('filename')
matriz_concatenada["Marca"] = matriz_concatenada.iloc[:, 0].apply(
    lambda x: 0 if str(x).endswith('_0.jpg') else (1 if str(x).endswith('_1.jpg') else None)
)
matriz_concatenada = matriz_concatenada.drop(matriz_concatenada.columns[-2], axis=1)
# Guardar el resultado en un nuevo archivo CSV
matriz_concatenada.to_csv("Matriz_Final.csv", index=False)

print("El archivo concatenado con la nueva columna ha sido guardado como 'Matriz_Final.csv'")
