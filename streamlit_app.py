import streamlit as st
import pandas as pd

st.title('MACHINE LEARNNG APP')

with st.expander('DATA'):
  st.write('**RAW DATA**')
df= pd.read_csv('https://raw.githubusercontent.com/Mawuyram/IDS/refs/heads/master/Final/IDS/lib/data/NSL-KDD.csv')
df
