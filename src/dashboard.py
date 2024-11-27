import streamlit as st

st.set_page_config(
    page_title="Inicio",
    page_icon="🏡",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={"Get Help": None, "Report a bug": None, "About": None}
)

st.title('Bem vindos ao projeto!')
st.write('Este é um projeto de exemplo para demonstrar o uso do Streamlit.')