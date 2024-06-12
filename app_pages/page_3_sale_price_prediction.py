import streamlit as st
import pandas as pd
import numpy as np
from src.data_management import load_pkl_file

def page_3_sale_price_prediction_body():

    # load predict sale price files
    version = "v1"
    sale_price_pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/best_regressor_pipeline.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv").columns.to_list())


    st.write("## Sale Price Prediction")
    st.success(
        "#### Business Requirement 2\n\n"
        "* The client is interested in predicting the house sale price from her four "
        "inherited houses and any other house in Ames, Iowa."
    )
