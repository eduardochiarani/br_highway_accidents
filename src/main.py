import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Leitura dataframes
df1 = pd.read_csv("../data/raw/2021.csv", sep=';', header=0, encoding='latin1')
df2 = pd.read_csv("../data/raw/2022.csv", sep=',', header=0)
df3 = pd.read_csv("../data/raw/2023.csv", sep=';', header=0, encoding='latin1')
df4 = pd.read_csv("../data/raw/2024.csv", sep=',', header=0)

df = pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True)

### Tratamento dos dados
# Retira linhas NaN e duplicadas
df = df.dropna()
df = df.drop_duplicates()

# Transformar data_inversa e horario -> datetime
df['data_inversa'] = pd.to_datetime(df['data_inversa'])
df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S')

### Engenharia de atributos - gerando variáveis
# periodo do dia entre 0 e 24 horas, com 4 valores: madrugada, manha, tarde e noite
df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S')
df['periodo_dia'] = pd.cut(df['horario'].dt.hour,
                           bins=[0, 6, 12, 18, 24],
                           labels=['Madrugada', 'Manhã', 'Tarde', 'Noite'],
                           include_lowest=True)
df['periodo_dia'] = df['periodo_dia'].astype('object')

# houve obito, não (0) ou sim (1)
df['houve_obito'] = df['mortos'].apply(lambda x: 1 if x > 0 else 0)

# houve vitimas, não (0) ou sim (1), considera feridos leves e graves, e óbitos como vítimas
df['houve_vitimas'] = df.apply(lambda row: 1 if (row['feridos_leves'] > 0) or
                                                (row['feridos_graves'] > 0) or
                                                (row['mortos'] > 0) else 0, axis=1)

# motoristas que ingeriram alcool, não (0) ou sim (1)
df['ing_alcool'] = np.where(df['causa_acidente'] == "Ingestão de álcool pelo condutor", 1, 0)

# motoristas que ingeriram alcool e se envolveram em acidente com vítimas, não (0) ou sim (1)
df['acidentes_com_ing_alcool'] = np.where((df['ing_alcool'] == 1) & (df['houve_vitimas'] == 1), 1, 0)

# # tipo de via, reta, curva ou outro
# df['reta_curva'] = np.where(df['tracado_via'].str.contains('Reta'), 'Reta',
#                             np.where(df['tracado_via'].str.contains('Curva'), 'Curva', 'Outro'))
# df = df[df['reta_curva'].isin(['Reta', 'Curva'])]


### PLOTS
fig, axs = plt.subplots(3, 1, figsize=(10, 30), gridspec_kw={'hspace': 1})

# Gráfico 1
ordem = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']
frequencia = df[(df['houve_vitimas'] == 1) & (df['acidentes_com_ing_alcool'] == 1)]['dia_semana'].value_counts().reindex(ordem)
axs[0].bar(frequencia.index, frequencia.values)
axs[0].set_xlabel('Dia-semana')
axs[0].set_ylabel('Frequência')
axs[0].set_title('Frequência de acidentes com vítimas devido à ingestão alcoólica, por Dia da Semana', ha='center')
axs[0].tick_params(axis='x', rotation=90)

# Gráfico 2
ordem = ['Madrugada', 'Manhã', 'Tarde', 'Noite']
frequencia = df[(df['houve_vitimas'] == 1) & (df['acidentes_com_ing_alcool'] == 1)]['periodo_dia'].value_counts().reindex(ordem)
axs[1].bar(frequencia.index, frequencia.values)
axs[1].set_xlabel('Períodos-dia')
axs[1].set_ylabel('Frequência')
axs[1].set_title('Frequência de acidentes com vítimas devido à ingestão alcoólica, por períodos do dia', ha='center')
axs[1].tick_params(axis='x', rotation=90)

# Gráfico 3
df_filtro = df.query('houve_vitimas == 1 and acidentes_com_ing_alcool == 1')
dados = df_filtro.groupby(['dia_semana', 'periodo_dia']).size().unstack()
dados = dados.reindex(['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado'])
dados = dados.reindex(columns=['Noite', 'Tarde', 'Manhã', 'Madrugada'])
cores = ['#007bff', '#34c759', '#f7dc6f', '#ffa07a', '#8e44ad']
dados.plot(kind='bar', stacked=True, color=cores, ax=axs[2])
axs[2].set_xlabel('Dia-semana')
axs[2].set_ylabel('Frequência')
axs[2].set_title('Frequência de acidentes com vítimas devido à ingestão alcoólica, por Dia da Semana e Período do Dia')
axs[2].legend(title='Período do Dia', loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=3, reverse=True)
axs[2].tick_params(axis='x', rotation=90)

plt.subplots_adjust()
plt.show()
