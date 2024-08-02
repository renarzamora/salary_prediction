import streamlit as st
import joblib
import numpy as np

st.title('Salary estimation App')
st.divider()

years_at_company = st.number_input('Enter years at the company',min_value=0, max_value=20)
satisfaction_level = st.number_input('Enter satisfaction level', min_value=0.0)
average_monthly_hours = st.number_input('Enter Average monthly hours', min_value = 120, max_value=400)

x = [years_at_company, satisfaction_level, average_monthly_hours]

scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

predict_button = st.button('Press for predicting salary')
st.divider()

if predict_button:
    x1 = np.array(x)
    x_array = scaler.transform([x1])
    prediction = model.predict(x_array)[0]
    st.write(f'Salary prediction is {prediction}')
    
else:
    st.write('Please enter the value and press the button to get the prediction')
