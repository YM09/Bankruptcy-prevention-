
import streamlit as st
import pickle

# Load the trained model
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

@st.cache_data()
def calc(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk):
    prediction = model.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
    return prediction

def main():
    st.title("Bankruptcy Prediction Application")
    st.image("image.jpg")

    # User input for risk factors
    st.sidebar.header("Input Risk Factors")
    industrial_risk = st.sidebar.radio('Industrial Risk', ('Low', 'Medium', 'High'))
    management_risk = st.sidebar.radio('Management Risk', ('Low', 'Medium', 'High'))
    financial_flexibility = st.sidebar.radio('Financial Flexibility', ('Low', 'Medium', 'High'))
    credibility = st.sidebar.radio('Credibility', ('Low', 'Medium', 'High'))
    competitiveness = st.sidebar.radio('Competitiveness', ('Low', 'Medium', 'High'))
    operating_risk = st.sidebar.radio('Operating Risk', ('Low', 'Medium', 'High'))

    # Analyze button
    if st.sidebar.button("Predict Bankruptcy"):
        prediction = calc(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk)
        st.markdown(f'<div style="color: green; font-size: 18px;">Prediction : {prediction[0]}</div>', unsafe_allow_html=True)
        

if __name__ == "__main__":
    main()
