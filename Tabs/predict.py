import streamlit as st

from web_functions import predict


def app(df, X, y):

    st.title("Página de predição")

    st.markdown(
        """
            <p style="font-size:25px">
                Este aplicativo usa <b style="color:green">Classificador de Floresta Aleatória</b> para a Previsão Precoce do Diabetes.
            </p>
        """, unsafe_allow_html=True)
    
    st.subheader("Selecionar valores:")

    fg = st.slider("Numero de Gravidez", int(df["Pregnancies"].min()), int(df["Pregnancies"].max()))
    ag = st.slider("Glicose", int(df["Glucose"].min()), int(df["Glucose"].max()))
    bp = st.slider("Hipertensão Arterial", int(df["BloodPressure"].min()), int(df["BloodPressure"].max()))
    sth = st.slider("Espessura da Pele", int(df["SkinThickness"].min()), int(df["SkinThickness"].max()))
    insulin = st.slider("Insulina", int(df["Insulin"].min()), int(df["Insulin"].max()))
    bmi = st.slider("IMC", float(df["BMI"].min()), float(df["BMI"].max()))
    gc = st.slider("Função Genetica", float(df["DiabetesPedigreeFunction"].min()), float(df["DiabetesPedigreeFunction"].max()))
    age = st.slider("Idade", int(df["Age"].min()), int(df["Age"].max()))

    features = [fg, ag, bp, sth, insulin, bmi, gc, age]

    if st.button("Predicao"):
        prediction, score = predict(X, y, features)
        score = score #correction factor
        st.info("Previsão realizada com sucesso")

        if (prediction == 1):
            st.warning("A pessoa tem alto risco de diabetes mellitus")
        else:
            st.success("A pessoa está livre de diabetes")

        st.write("O modelo utilizado é de confiança do médico e tem uma precisão de ", (score*100),"%")
