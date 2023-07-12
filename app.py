import streamlit as st
import pickle
import calendar
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Augest', 'September', 'October', 'November', 'December']

st.title("Weather Predictor")

st.text("\n")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)


with col1:
    max_temp = st.number_input("Enter The Maximum Temprature")

with col2:
    min_temp = st.number_input("Enter The Minimum Temprature")

with col3:
    wind = st.number_input("Enter The Wind Speed")

with col4:
    month = st.selectbox("Select The Month", months)

if st.button("Predict"):
    month_number = list(calendar.month_name).index(month.capitalize())
    data = [[max_temp, min_temp, wind, month_number]]
    df = pd.DataFrame(data)
    prediction = model.predict(df)

    if prediction[0] == 0:
        prediction = "Drizzle"

    elif prediction[0] == 1:
        prediction = "Fog"

    elif prediction[0] == 2:
        prediction = "Rain"
    
    elif prediction[0] == 3:
        prediction = "Snow"
    
    else:
        prediction = "Sunny"
    
    st.write(f"## {prediction}") 
