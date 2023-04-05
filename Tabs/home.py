"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("TCC sobre Diabetes")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            O diabetes é uma condição de saúde crônica (de longa duração) que afeta a forma como seu corpo transforma alimentos em energia.
            Ainda não existe cura para o diabetes, mas perder peso, comer alimentos saudáveis e ser ativo pode realmente ajudar a reduzir o impacto do diabetes.
            Este aplicativo da Web ajudará você a prever se uma pessoa tem diabetes ou está propensa a ter diabetes no futuro, analisando os valores de vários recursos usando o Random Forest Classifier.
        </p>
    """, unsafe_allow_html=True)
