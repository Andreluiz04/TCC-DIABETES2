import streamlit as st


def app(df):
    st.title("Pagina de Informações dos dados")
    st.subheader("Visualizar Dados")

    with st.expander("Visualizar Dados"):
        st.dataframe(df)

    st.subheader("Descrição das Colunas:")

    if st.checkbox("Visualizar Sumario"):
        st.dataframe(df.describe())

    col_name, col_dtype, col_data = st.columns(3)

    with col_name:
        if st.checkbox("Nome das Colunas"):
            st.dataframe(df.columns)

    with col_dtype:
        if st.checkbox("Tipo de Dados das Colunas"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)

    with col_data: 
        if st.checkbox("Dados das Colunas"):
            col = st.selectbox("Nome das Colunas", list(df.columns))
            st.dataframe(df[col])

