import pandas as pd
import streamlit as st
import functions
import joblib

st.title("Alkuwaiti Group Demand Prediction")
#load rf model
model = joblib.load("model.pkl")

#input 
sku= st.selectbox("Select Product",
 ["ICE-100","ICE-200","CH-600","FR-600","OV-6T", "AC-18","DRY-8KG"])

cat= st.selectbox("Select Category",
                  ["Cooling","Cooking","Landry"])

month = st.selectbox("Select Month",list(range(1,13)))

year= st.number_input("Select Year", value=2026, min_value=2021)

prev_sales= st.number_input("Select Previous Month Sales in units",min_value=0)

#predict button
if st.button("Predict Demand"):
    input_data= pd.DataFrame({
        "SKU":[sku],
        "Category":[cat],
        "Month_Num": [month],
        "Year":[year],
        "Prev_sales": [prev_sales]
    })
    pred= model.predict(input_data)[0]
    st.success(f"Predicted Demand for Product{sku} is {pred} units")
