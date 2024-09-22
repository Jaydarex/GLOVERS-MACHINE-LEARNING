import streamlit as st
import pandas as pd

st.title('🎈 App Name')

st.write('Hello world!')
df= pd.read_csv('https://raw.githubusercontent.com/Mawuyram/IDS/refs/heads/master/Final/IDS/lib/data/KDDTest%2B.arff.csv ')
df
