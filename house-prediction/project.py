import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression
import pickle


st.image("ino_img.jpg",width = 200)

st.title("HOUSE PRICE PREDICTION")
model = pickle.load(open("lr.pkl","rb"))
 


SquareFeet = st.number_input("Enter the size of house",min_value = 300, max_value = 3500,step = 50)	
Bedrooms = st.number_input("Enter the no of bedrooms",min_value = 0,max_value = 5,step = 1)	
Bathrooms = st.number_input("Enter the no of bathrooms",min_value = 0,max_value = 6,step =1)	
Neighborhood = st.radio("Enter the neighborhood",["Rural","Urban","Suburb"])
neighbor = 1 if Neighborhood == "Rural" else 2 if Neighborhood == "Urban" else 3

YearBuilt = st.number_input("Enter the number of year of constructin",min_value = 2023, max_value = 2060,step = 1)


if st.button("PREDICT PRICE"):
    try:
        price = model.predict([[SquareFeet, Bedrooms, Bathrooms, neighbor, YearBuilt]])
        st.write("The price for the flat with given details is Rs.", price[0])
    except Exception as e:
        st.error("An error occurred during prediction:")
        st.error(e)
