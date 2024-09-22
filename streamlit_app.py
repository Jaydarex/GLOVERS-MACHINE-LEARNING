import streamlit as st
import pandas as pd

st.title('MACHINE LEARNNG APP')
df= pd.read_csv('https://raw.githubusercontent.com/Mawuyram/IDS/refs/heads/master/Final/IDS/lib/data/KDDTest%2B.arff.csv ')
df
