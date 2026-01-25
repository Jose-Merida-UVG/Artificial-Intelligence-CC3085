import numpy as np
import pandas as pd

# 1. Dirty dataset generation

# Initialize empty list of dictionaries to store data
data_list = []

# Add 100 entries
for i in range(100):
    # Initialize row with random values, all '0's initially for 'Compro_Producto'
    row = {
        "Edad": np.random.randint(16, 90),
        "Salario": np.random.uniform(4000, 50000),
        "Compro_Producto": 0,
    }
    # Add row to list
    data_list.append(row)

# Turn list into DF
df = pd.DataFrame(data_list)

# Set 10 random entries in 'Edad' to NaN
df.loc[df.sample(10).index, "Edad"] = np.nan

# Set 10 random samples in 'Compro_Producto' to '1'
df.loc[df.sample(10).index, "Compro_Producto"] = 1

# Print dimensions / properties to verify
print("1. Generacion Dataset Sucio")

print(
    f"Filas: {df.shape[0]} | Columnas: {df.shape[1]} | Nulls en Edad: {df['Edad'].isnull().sum()} | Compro_Producto con '1': {df['Compro_Producto'].sum()}"
)

# 2. Data Inputter

# Calculate mean for 'Edad' column
mean = df["Edad"].mean()

# Manually iterate through all rows replacing nans, bajillion built-in functions for this but it's instructions
# This is also slower as far as I know but learning purposes & stuff
for i, row in df.iterrows():
    if pd.isna(row["Edad"]):
        df.at[i, "Edad"] = mean

new_mean = df["Edad"].mean()

print("2. Imputacion")

print(f"Nulls en Edad: {df['Edad'].isnull().sum()}")

print(
    f"Media Anterior: {mean:.2f} | Nueva Media: {new_mean:.2f} | Diferencia: {(mean - new_mean):.2f} | Son iguales si la imputacion se realizo correctamente"
)

# Pregunta extra: ¿En que situación usar el promedio sería una mala idea y sería mejor utilizar la mediana?

# El promedio es una mala idea si se tienen outliers extremos. Por ejemplo, para la lista [1,1,x,1000]
# (a parte de probablemente ser un error de entrada) el promedio es de 334 mientras que viendo los datos
# crudos la mejor idea podría ser un valor cercano a 1. También se puede tomar un "approach" más visual
# y basarse en la longitud de las colas para identificar el sesgo. Otro ejemplo sería el salaio o ingresos
# mensuales promedios en USA donde el top 0.1% tiene del 13-14% de las riquezas. Aquí el promedio y
# mediana de los ingresos son $75000 y $55000 aproximadamente, definitivamente deberíamos utilizar la
# mediana.

# 3. Unbalanced data management


# Function to balance the dataset
def undersample(df, target, min, maj):
    minority = df[df[target] == min]
    majority = df[df[target] == maj]

    n_min = len(minority)

    majority_sample = majority.sample(n=n_min)

    balanced_df = pd.concat([minority, majority_sample])

    return balanced_df


# Balance the dataset
balanced_df = undersample(df, "Compro_Producto", 1, 0)

print("3. Manejo de datos desbalanceados")

print(
    f"Filas: {balanced_df.shape[0]} | Compro_Producto con '1': {balanced_df['Compro_Producto'].sum()} | Compro_Producto con '0' {balanced_df.shape[0] - balanced_df['Compro_Producto'].sum()}"
)
