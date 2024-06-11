import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_data():
    df = pd.read_csv("outputs/datasets/collection/house_prices_records.csv")
    return df


def load_inherited_houses_data():
    inherited_df = pd.read_csv("outputs/datasets/collection/inherited_houses.csv")
    return inherited_df
