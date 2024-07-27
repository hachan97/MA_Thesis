import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri

st.title("Welcome to my Master's Thesis Project")

st.header("Haoting's Master Thesis")
'''
Hello! I'm excited to share with you my journey in exploring the fascinating world of **Legal Language Modeling (LLM)** and the **United Nations Security Council (UNSC) speech database**. This project is a part of my Master's thesis and is my first venture into using Streamlit, a fast and easy way to create web apps for machine learning and data science.

In this project, we will delve into the intricacies of legal language as used in the UNSC speeches. We aim to understand the patterns, nuances, and implications of the language used in these speeches. Our goal is to develop a language model that can effectively interpret and generate legal language, providing valuable insights into international law and diplomacy.

Stay tuned as we embark on this exciting journey of discovery and learning. Your feedback and suggestions are most welcome as they will help improve the project. Thank you for visiting!
'''

st.header("Insights into the UNSC Dataset")
# Insights into the UNSC Dataset
df_UNSC_meta_speeches = pd.read_csv('data/df_UNSC_meta_speeches.csv')

# Add a slider to the sidebar for 'year':
selected_years = st.sidebar.slider(
    'Select a range of years',
    int(df_UNSC_meta_speeches['year'].min()), int(df_UNSC_meta_speeches['year'].max()), (int(df_UNSC_meta_speeches['year'].min()), int(df_UNSC_meta_speeches['year'].max()))
)

# Filter the dataframe based on the selected range of years
df_filtered = df_UNSC_meta_speeches[(df_UNSC_meta_speeches['year'] >= selected_years[0]) & (df_UNSC_meta_speeches['year'] <= selected_years[1])]

# Frequency of each unique value in the "topic2" column 
topic2_counts = df_filtered['topic2'].value_counts().head(10)

# Plotting
plt.figure(figsize=(18, 10))
topic2_counts.plot(kind='bar')
plt.xlabel('Topics')
plt.ylabel('Frequency')
plt.title(f'Frequency of Each Topic from {selected_years[0]} to {selected_years[1]}', fontsize=30)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)
