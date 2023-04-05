import warnings
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import tree
import streamlit as st

from web_functions import train_model

def app(df, X, y):
  
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("VISUALIZAR APP DE DIABETES")

    if st.checkbox("MOSTRAR MAPA DE CORRELAÇÃO"):
        st.subheader("MAPA DE CORRELAÇÃO")

        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)  
        bottom, top = ax.get_ylim()                             
        ax.set_ylim(bottom + 0.5, top - 0.5)                    
        st.pyplot(fig)

    if st.checkbox("Gráfico de Numero de gestação vs Pressão Arterial"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="Pregnancies",y="BloodPressure",data=df)
        st.pyplot()

    if st.checkbox("Gráfico de nível de glicose versus pressão arterial"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="Glucose",y="BloodPressure",data=df)
        st.pyplot()

    if st.checkbox("Gráfico de Nível de Pressão Arterial vs Espessura da Pele"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="BloodPressure",y="SkinThickness",data=df)
        st.pyplot()

    if st.checkbox("Mostrar histograma"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.histplot(data=df,x="Age",y="BloodPressure")
        st.pyplot()

    if st.checkbox("Plotar Árvore de Decisão"):
        model, score = train_model(X, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=X.columns, class_names=['0', '1']
        )
        st.graphviz_chart(dot_data)

