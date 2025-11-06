import pandas as pd
import streamlit as st

st.header("Displaying dataframes")

data = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age' : [21, 22, 23, 24, 25],
    'City' : ['NewYork', 'NewZeland', 'Chicago', 'SanAndreas', 'SF']
             })
st.dataframe(data)

