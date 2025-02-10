import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Review",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={"Get Help": None, "Report a bug": None, "About": None}
)


st.title('Bem vindos ao projeto de análise de ocorrência de acidentes em rodovias federais do Brasil!')
st.write("""
- **O que o projeto aborda:** Acidentes registrados por dados abertos da PRF ocorridos entre 2021 e 2024;
- **Técnicas aplicadas:** Análise e engenharia de dados para gerar insights visuais via streamlit;
- **Análise 1:** Validação de dataset;
- **Análise 2:** Acidentes com vítimas devido à ingestão de álcool, comportamento do fenômeno ao longo dos dias da semana e períodos do dia.
- **Análise 3:** Mapa de localização e mapa de calor dos acidentes da análise 2;
""")
