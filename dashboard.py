import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import norm
import altair as alt

st.set_page_config(
    page_title="EDA No-Code", page_icon="📊", initial_sidebar_state="expanded"
)

st.write(
    """
# 📊 EDA No-Code
Upload your CSV document for an Exploratory Data Analysis.
"""
)

uploaded_file = st.file_uploader("Upload CSV", type=".csv")

ft_default = None
result_default = None

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### Data preview")
    st.dataframe(df.head())

    st.markdown("### Select columns for analysis")
    with st.form(key="my_form"):
        ft = st.multiselect(
            "Data column",
            options=df.columns,
            help="Select which column refers to the feature your are exploring.",
            default=ft_default,
        )
