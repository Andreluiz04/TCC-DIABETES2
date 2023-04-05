#para rodar utilizar o comando: python -m streamlit run main.py
import streamlit as st
from web_functions import load_data
from Tabs import home, data, predict, visualise

st.set_page_config(
    page_title = 'TCC sobre Diabetes',
    page_icon = 'random',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

Tabs = {
    "PAGINA INICIAL": home,
    "INFORMAÇÃO SOBRE OS DADOS": data,
    "PREDIÇÃO": predict,
    "VISUALIZAÇÃO": visualise
}

st.sidebar.title("NAVEGAÇÃO")

page = st.sidebar.radio("PAGINAS", list(Tabs.keys()))

df, X, y = load_data()

if page in ["PREDIÇÃO", "VISUALIZAÇÃO"]:
    Tabs[page].app(df, X, y)
elif (page == "INFORMAÇÃO SOBRE OS DADOS"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
