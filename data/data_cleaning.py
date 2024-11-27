import pandas as pd

# Leitura dataframes
df1 = pd.read_csv("raw/2021.csv", sep=';', header=0, encoding='latin1')
df2 = pd.read_csv("raw/2022.csv", sep=';', header=0, encoding='latin1')
df3 = pd.read_csv("raw/2023.csv", sep=';', header=0, encoding='latin1')
df4 = pd.read_csv("raw/2024.csv", sep=';', header=0, encoding='latin1')

# Concatenar dataframes
df_concat = pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True)

# Retirar linhas NaN e duplicadas
df_concat = df_concat.dropna()
df_concat = df_concat.drop_duplicates()

# Transformar data_inversa -> datetime -> dt.date
df_concat['data_inversa'] = pd.to_datetime(df_concat['data_inversa'])
df_concat['data_inversa'] = df_concat['data_inversa'].dt.date

# Transformar horario -> datetime -> dt.time
df_concat['horario'] = pd.to_datetime(df_concat['horario'], format='%H:%M:%S')
df_concat['horario'] = df_concat['horario'].dt.time

# Transformar br int64 -> object
df_concat['br'] = df_concat['br'].astype('object')

# Salvar dataframe em data/processed
df_concat.to_csv("processed/df_concat.csv", index=False)
