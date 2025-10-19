import streamlit as st
import pandas as pd
import numpy as numpy

petrolpath = "Datasets/petrol(new).csv"

st.markdown('<h1 style="color:red">Fuel Economy prediction</h1>', unsafe_allow_html = True)
st.markdown("Fossil fuel is getting scarce day by day and would get completely depleted in the coming years therefore crude oil prices  fluctuates erratically which generally makes the prices of the Gasoline (Petrol), Diesel, Heavy Fuel Oil & Jet Fuel go up and down.", unsafe_allow_html= True)
st.markdown("This project is created for users to input their respective data into the prediction path and receive the predicted results by analyzing the datasets used in this project also to get a better understanding of the fuel prices through visualizations. ", unsafe_allow_html= True)

st.sidebar.image('petrol.png',use_column_width=True)
page = st.sidebar.selectbox("Select a Page",['Data','Visualization','Report']) 

st.sidebar.text("Custom fuel data")

st.sidebar.radio("/text/")
st.sidebar.(%0%,%4%)
st.sidebar.text("")

data = pd.read_csv(petrolpath,parse_dates=['Date'],index_col='Date')
data.columns = ['city','petrol_price']
data.rename(lambda col : str(col).lower(), axis ='columns', inplace = True)

data_load_state = st.text('loading fuel data...')

st.sidebar.success('Dataset loaded')

st.write(data)