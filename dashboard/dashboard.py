import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Air Quality Data Analysis Dashboard')

st.sidebar.title('Options')
selected_option = st.sidebar.selectbox('Choose a chart to display:', ['PM2.5 Monthly Average', 'Temperature vs. PM2.5'])

@st.cache_data
def load_data():
    data = pd.read_csv('main_data.csv')

    data['No'] = pd.to_numeric(data['No'], errors='coerce').fillna(0).astype(int)
    
    data['date'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
    
    return data

data = load_data()

if selected_option == 'PM2.5 Monthly Average':
    st.subheader('PM2.5 Monthly Average')

    monthly_pm25 = data.groupby('month')['PM2.5'].mean()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_pm25.index, monthly_pm25.values, marker='o')
    plt.title('Average PM2.5 Levels by Month')
    plt.xlabel('Month')
    plt.ylabel('PM2.5 Levels')
    st.pyplot(plt)

if selected_option == 'Temperature vs. PM2.5':
    st.subheader('Temperature vs. PM2.5')

    plt.figure(figsize=(10, 6))
    plt.scatter(data['TEMP'], data['PM2.5'], alpha=0.5)
    plt.title('Temperature vs. PM2.5 Levels')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('PM2.5 Levels')
    st.pyplot(plt)

