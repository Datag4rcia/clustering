import streamlit as st
import pandas as pd 
st.set_page_config(page_title="Dashboard Wine")

with st.container():
    st.subheader("Análise de dados com vinhos")


@st.cache_data
def carregar_dados():
    tabela = pd.read_excel("wine_data.xlsx")
    return tabela

with st.container():
    st.write("---")
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")
