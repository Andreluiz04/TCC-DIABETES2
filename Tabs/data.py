"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st


def app(df):
    """This function create the Data Info page"""

    # Add title to the page
    st.title("Pagina de Informações dos dados")

    # Add subheader for the section
    st.subheader("Visualizar Dados")

    # Create an expansion option to check the data
    with st.expander("Visualizar Dados"):
        st.dataframe(df)

    # Create a section to columns values
    # Give subheader
    st.subheader("Descrição das Colunas:")

    # Create a checkbox to get the summary.
    if st.checkbox("Visualizar Sumario"):
        st.dataframe(df.describe())

    # Create multiple check box in row
    col_name, col_dtype, col_data = st.columns(3)

    # Show name of all dataframe
    with col_name:
        if st.checkbox("Nome das Colunas"):
            st.dataframe(df.columns)

    # Show datatype of all columns 
    with col_dtype:
        if st.checkbox("Tipo de Dados das Colunas"):
            dtypes = df.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)
    
    # Show data for each columns
    with col_data: 
        if st.checkbox("Dados das Colunas"):
            col = st.selectbox("Nome das Colunas", list(df.columns))
            st.dataframe(df[col])

