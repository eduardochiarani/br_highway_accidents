import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import seaborn as sns

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="auto",
)

# Função para exibir o gráfico
def exibir_grafico(data, xlabel, ylabel, title):
    st.write("### Gráfico de Barras:")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data.index, data.values, color='skyblue')
    ax.set_xlabel(xlabel, color='white')
    ax.set_ylabel(ylabel, color='white')
    ax.set_title(title, ha='center', color='white')
    ax.tick_params(axis='x', rotation=90, colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.set_facecolor((1, 1, 1, 0.05))
    fig.patch.set_alpha(0.02)
    st.pyplot(fig)

# Conteúdo da página
st.title('Análise de Dados')
st.markdown('> O objeto de análise deste projeto foi o de acidentes de trânsito com vítimas devidos à ingestão de bebida alcoólica.\
    Nesta página, temos várias análises quanto a .........')

df = pd.read_csv('./data/processed/df_concat.csv')

# TODO: onde colocar esses processamentos dos dados
df['acidentes_com_ing_alcool'] = np.where(
    ((df['feridos_leves'] > 0) | (df['feridos_graves'] > 0) | (df['mortos'] > 0)) & 
    (df['causa_acidente'] == "Ingestão de álcool pelo condutor"), 1, 0)

df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S')
df['periodo_dia'] = pd.cut(df['horario'].dt.hour,
                           bins=[0, 6, 12, 18, 24],
                           labels=['Madrugada', 'Manhã', 'Tarde', 'Noite'],
                           include_lowest=True)
df['periodo_dia'] = df['periodo_dia'].astype('object')

st.write("### Amostra:")
st.table(df[df['acidentes_com_ing_alcool'] == 1].head(2))

ordem = ['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado']
data = df[df['acidentes_com_ing_alcool'] == 1]['dia_semana'].value_counts().reindex(ordem, fill_value=0)
xlabel = ""
ylabel = ""
title = ""
exibir_grafico(data, xlabel, ylabel, title)

ordem = ['Madrugada', 'Manhã', 'Tarde', 'Noite']
data = df[df['acidentes_com_ing_alcool'] == 1]['periodo_dia'].value_counts().reindex(ordem)
xlabel = ""
ylabel = ""
title = ""
exibir_grafico(data, xlabel, ylabel, title)



# TODO: gráfico especifico
#filtra dataframee agrupa os dados
data = df[(df['acidentes_com_ing_alcool'] == 1)].groupby(['dia_semana', 'periodo_dia']).size().unstack()
data = data.reindex(['domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado'])
data = data.reindex(columns=['Noite', 'Tarde', 'Manhã', 'Madrugada'])
cores = ['#007bff', '#34c759', '#f7dc6f', '#ffa07a']
fig, axs = plt.subplots(figsize=(10, 6))
data.plot(kind='bar', stacked=True, color=cores, ax=axs)
axs.set_xlabel('Dia da Semana', color='white')
axs.set_ylabel('Frequência', color='white')
axs.set_title('Frequência de acidentes com vítimas devido a ingestão alcoólica, por Dia da Semana e Período do Dia', color='white')
axs.legend(title='Período do Dia', loc='upper center', bbox_to_anchor=(0.5, 1.00), ncol=3, reverse=True,
           labelcolor='white', title_fontsize='13', frameon=False)
axs.tick_params(axis='x', rotation=90, labelcolor='white')
axs.tick_params(axis='y', labelcolor='white')
axs.set_facecolor((1, 1, 1, 0.05))
fig.patch.set_alpha(0.02)
st.write("### Gráfico de Barras:")
st.pyplot(fig)


# sns.scatterplot(
#     data = data,
#     x ='Dia-semana',
#     y ='Frequência',
#     ax = ax
# )
# st.pyplot(fig)

# # Métricas resumidas
# c1, c2 = st.columns(2)
# c1.metric("Média", round(df['Valores'].mean(), 2))
# c2.metric("Máximo", df['Valores'].max())
