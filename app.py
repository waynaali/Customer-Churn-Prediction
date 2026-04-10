import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go

# -------------------------
# Gauge Function
# -------------------------
def create_gauge(prob):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Churn Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#444444"}
            'steps': [
                {'range': [0, 40], 'color': "green"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ]
        }
    ))
    return fig


# -------------------------
# Page setup
# -------------------------
st.set_page_config(page_title='Customer Churn Predictor', layout='wide')
st.title('Customer Churn Prediction System')


# -------------------------
# Load model
# -------------------------
@st.cache_resource
def load_model():
    with open('best_churn_model.pkl', 'rb') as file:
        return pickle.load(file)

model_data = load_model()
model = model_data["model"]
model_columns = model_data["columns"]

st.success("Model loaded successfully!")


# -------------------------
# Inputs
# -------------------------
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox('Gender', ['Male', 'Female'])
    senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])

with col2:
    tenure = st.slider('Tenure (months)', 0, 72, 12)
    monthly_charges = st.number_input('Monthly Charges', 0.0, 200.0, 70.0)


# -------------------------
# Prediction
# -------------------------
if st.button('Predict Churn'):

    # input data
    input_data = {
        'gender': gender,
        'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges
    }

    input_df = pd.DataFrame([input_data])

    # one-hot encoding
    input_encoded = pd.get_dummies(input_df)

    # match training columns
    for col in model_columns:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    input_encoded = input_encoded[model_columns]

    # prediction
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0]
    churn_prob = probability[1] * 100


    # -------------------------
    # OUTPUT SECTION (FIXED)
    # -------------------------
    st.subheader("📊 Risk Analysis Dashboard")

    st.metric("Churn Probability", f"{churn_prob:.1f}%")

    if prediction == 1:
        st.error("⚠️ High Risk Customer")
    else:
        st.success("✅ Low Risk Customer")

    st.plotly_chart(create_gauge(churn_prob / 100))
