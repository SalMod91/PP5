import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns

def page_2_sale_price_study_body():

    df = load_house_data()

    st.write("## Sale Price Study")
    st.info(
        f"#### Business Requirement 1\n\n"
        f"* The client is interested in discovering how the house attributes correlate "
        f"with the **Sale Price**. Therefore, the client expects data visualizations"
        f" of the correlated variables against the sale price to show that."
    )

    if st.checkbox("Inspect Dataset"):
        st.write(
            f"The dataset has {df.shape[0]} rows and {df.shape[1]} columns.\n\n"
            f"Displayed below are the first 10 rows of the dataset.")
        
        st.write(df.head(10))
