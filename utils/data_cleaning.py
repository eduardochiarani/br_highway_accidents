import pandas as pd

# Leitura dataframes
df1 = pd.read_csv("../data/2021.csv", sep=';', header=0, encoding='latin1')
df2 = pd.read_csv("../data/2022.csv", sep=',', header=0)
df3 = pd.read_csv("../data/2023.csv", sep=';', header=0, encoding='latin1')
df4 = pd.read_csv("../data/2024.csv", sep=',', header=0)

# Concatenar dataframes
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)
print(len(df_concat))

# Retirar linhas NaN e duplicadas
df_concat = df_concat.dropna()
print(len(df_concat))
df_concat = df_concat.drop_duplicates()
print(len(df_concat))

# Transformar data_inversa -> datetime -> dt.date
df_concat['data_inversa'] = pd.to_datetime(df_concat['data_inversa'])
df_concat['data_inversa'] = df_concat['data_inversa'].dt.date
# Transformar horario -> datetime -> dt.time
df_concat['horario'] = pd.to_datetime(df_concat['horario'], format='%H:%M:%S')
df_concat['horario'] = df_concat['horario'].dt.time
