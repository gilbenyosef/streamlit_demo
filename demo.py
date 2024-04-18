import streamlit as st
import pandas as pd
import numpy as np

st.title("hello streamlit 2.1")

# data = pd.read_csv('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz', nrows=100)

# lowercase = lambda x: str(x).lower()
# data.rename(lowercase, axis='columns', inplace=True)
# data['date/time'] = pd.to_datetime(data['date/time'])
    
data = pd.read_csv('data.csv')
st.subheader('Raw Data')
st.write(data)

st.subheader('Map')
st.map(data)
