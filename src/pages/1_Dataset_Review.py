import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto",
)

df = pd.read_csv('./data/processed/df_concat.csv')

st.title('Datasets')
st.markdown('> 🧹 Foi realizado um pré-processamento no conjuto de dados.\
    Unindo os anos 2021 à 2024, bem como a limpeza dos dados removendo nulos e duplicados.')
st.markdown('> 👁‍🗨 Para mais detalhes veja o script ``data_cleaning.py``')
st.markdown('#### Resultado da limpeza')

# Linha detalhes
c1, c2, c3, c4 = st.columns(4)
c1.metric("Observações", df.shape[0])
c2.metric("Atributos", df.shape[1])
c3.metric("Nulos removidos", df.shape[1])
c4.metric("Duplicados removidos", df.shape[1])

# 
st.markdown('##### Amostra de exemplo (10 registros)')
st.write(df.head(10))