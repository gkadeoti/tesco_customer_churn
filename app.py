## This is going to be a Streamlit App

import streamlit as st
import pandas as pd
from autogluon.tabular import TabularPredictor


st.title('Tesco Customer Churn Prediction')

gender = st.selectbox('gender', ['Female', 'Male'])
seniorcitizen = st.selectbox('seniorcitizen', options=['0','1'])
partner = st.selectbox('partner', options=['Yes','No'])
dependents = st.selectbox('dependents', options=['Yes','No'])
tenure = st.number_input('tenure', 0, 100)
phoneservice = st.selectbox('phoneservice', options=['Yes','No'])
multiplelines = st.selectbox('multiplelines', options=['Yes','No'])
internetservice = st.selectbox('internetservice', options=['DSL','No','Fibre optic'])
onlinesecurity = st.selectbox('onlinesecurity', options=['Yes','No','No internet service']) 
onlinebackup = st.selectbox('onlinebackup', options=['Yes','No','No internet service'])
deviceprotection = st.selectbox('deviceprotection', options=['Yes','No','No internet service'])
techsupport = st.selectbox('techsupport', options=['Yes','No','No internet service'])
streamingtv = st.selectbox('streamingtv', options=['Yes','No','No internet service'])
streamingmovies = st.selectbox('streamingmovies', options=['Yes','No','No internet service'])
contract = st.selectbox('contract', options=['Month-to-month', 'Two year', 'One year'])
paperlessbilling = st.selectbox('paperlessbilling', options=['Yes', 'No'])
paymentmethod = st.selectbox('paymentmethod',
                                 options=['Electronic check',
                                            'Bank transfer (automatic)',
                                          'Mailed check', 'Credit card (automatic)'])
monthlycharges = st.number_input('monthlycharges', 0, 200)
totalcharges = st.number_input('totalcharges', 0, 10000)

input_data_dict = {
    'gender': gender,
    'seniorcitizen': seniorcitizen,
    'partner': partner,
    'dependents': dependents,
    'tenure': tenure,
    'phoneservice': phoneservice,
    'multiplelines': multiplelines,
    'internetservice': internetservice,
    'onlinesecurity': onlinesecurity,
    'onlinebackup': onlinebackup,
    'deviceprotection' : deviceprotection,
    'techsupport': techsupport,
    'streamingtv': streamingtv,
    'streamingmovies': streamingmovies,
    'contract': contract,
    'paperlessbilling': paperlessbilling,
    'paymentmethod': paymentmethod,
    'monthlycharges': monthlycharges,
    'totalcharges': totalcharges
}

st.write(input_data_dict)

input_data = pd.DataFrame([input_data_dict])

st.write(input_data)

save_path = "models"

save_model_predictor = TabularPredictor.load(save_path) #unnecessary

submit = st.button("CLICK HERE TO PREDICT CUSTOMER CHURN")

if submit:
    churn_prediction = save_model_predictor.predict(input_data)[0]
    st.write(f"The churn prediction is: {churn_prediction}")
