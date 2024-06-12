import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
from src.data_management import load_pkl_file, load_house_data
from src.machine_learning.predictive_analysis_ui import predict_sale_price

def page_3_sale_price_prediction_body():
    """
    This function handles the sale price prediction page, loading models,
    generating input widgets, and displaying business requirements.
    """

    # Load the prediction model and feature set for a specified version
    version = "v1"
    sale_price_pipeline = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/best_regressor_pipeline.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv").columns.to_list())

    # Header
    st.write("## Sale Price Prediction")

    # Business Requirement
    st.success(
        "#### Business Requirement 2\n\n"
        "* The client is interested in predicting the house sale price from her four "
        "inherited houses and any other house in Ames, Iowa."
    )

    # Generate live input data using widgets
    X_live = DrawInputsWidgets()

    # Predict live data
    if st.button("Run Predictive Analysis"): 
        prediction = predict_sale_price(X_live, sale_price_features, sale_price_pipeline)
        st.write(f"Estimated Sale Price: **${prediction:,}**")
    
    st.write("---")

def DrawInputsWidgets():
    """
    Generates interactive input widgets for user to input feature values for prediction
    and returns the DataFrame with these input values.
    """

    # Load the dataset to get median values for default inputs
    df = load_house_data()
    # Define percentage bounds for input limits
    percentageMin, percentageMax = 0.4, 2.0

    # Empty DataFrame to store live input data
    X_live = pd.DataFrame(index=[0])

    # Create Input Widgets for the best features
    col1, col2, col3 = st.beta_columns(3)

    # Widget for Overall Quality
    with col1:
        feature = "OverallQual"
        label = "Overall Quality (1-10)"
        median_val = int(df[feature].median())
        step = 1
        st_widget = st.number_input(label=label, min_value=1, max_value=10, value=median_val, step=step)
        
    
    X_live[feature] = st_widget
    
    # Widget for Ground Living Area
    with col2:
        feature = "GrLivArea"
        label = "Ground Living Area (sq ft)"
        median_val = int(df[feature].median())
        step = 100
        st_widget = st.number_input(label=label, min_value=int(df[feature].min()*percentageMin), max_value=int(df[feature].max()*percentageMax), value=median_val, step=step)
        
    
    X_live[feature] = st_widget

    # Widget for Year Built
    with col3:
        feature = "YearBuilt"
        label = "Year Built"
        median_val = int(df[feature].median())
        step = 1
        st_widget = st.number_input(label=label, min_value=int(df[feature].min()*percentageMin), max_value=date.today().year, value=median_val, step=step)


    
    X_live[feature] = st_widget


    # Create the second row of columns
    col4, col5, col6 = st.beta_columns(3)

    # Widget for Garage Area
    with col4:
        feature = "GarageArea"
        label = "Garage Area (sq ft)"
        median_val = int(df[feature].median())
        step = 100
        st_widget = st.number_input(label=label, min_value=int(df[feature].min()*percentageMin), max_value=int(df[feature].max()*percentageMax), value=median_val, step=step)

    
    X_live[feature] = st_widget

    # Widget for Total Basement SF
    with col5:
        feature = "TotalBsmtSF"
        label = "Total Basement Area (sq ft)"
        median_val = int(df[feature].median())
        step = 100
        st_widget = st.number_input(label=label, min_value=int(df[feature].min()*percentageMin), max_value=int(df[feature].max()*percentageMax), value=median_val, step=step)
    
    X_live[feature] = st_widget

    return X_live
