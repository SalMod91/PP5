import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_management import (
    load_house_data,
    load_pkl_file
)

from src.machine_learning.evaluate_regression import (
    regression_evaluation,
    regression_performance,
    regression_evaluation_plots
)


def page_5_ml_model_body():
    """
    Streamlit page handler for displaying the
    machine learning model's performance metrics,
    feature importances, and evaluation plots.
    """

    # Load model and feature data
    version = "v1"
    sale_price_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/"
        f"best_regressor_pipeline.pkl"
    )

    sale_price_features = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv"
    ).columns.to_list()

    feature_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/"
        f"features_importance.png"
    )

    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv"
    )

    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv"
    )

    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv"
    )

    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv"
    )

    # Display the title and introductory information
    st.write("## Machine Learning Model")
    st.info(
        "A machine learning model has been developed to"
        " predict house sale prices in Ames, Iowa.\n "
        "The model utilizes the ExtraTreesRegressor algorithm,"
        " a linear regressor.\n\n We initially used "
        "a regressor model to predict the sale price and attempted"
        " to improve its performance with PCA, "
        "but this did not yield better results.\n\n"
        " The initial dataset was comprised of 23 features. We dropped "
        "two variables that had approximately 90% missing data."
        " Additionally, we removed GarageYrBlt due to "
        "its strong correlation with YearBuilt and YearRemodAdd,"
        " which caused redundancy. Further feature "
        "engineering and smart correlated selection led to the removal of"
        " another variable, **1stFlrSF**.\n\n The "
        "model was then tuned using a hyperparameter as shown in"
        " the ML pipeline below,"
        " achieving a training score of 0.934 and a test score of 0.844."
    )

    # Show the code for the loaded pipeline
    st.write("### ML Model Pipeline")
    st.code(sale_price_pipeline)
    st.write("---")

    st.write("### The features the Model was trained on and their importance")
    # Display the features used by the model
    st.write(X_train.columns.to_list())
    # Display feature importance image
    st.image(feature_importance)
    st.write("---")

    # Evaluate and display the model's performance on training and test data
    regression_performance(
        X_train=X_train,
        y_train=y_train,
        X_test=X_test,
        y_test=y_test,
        pipeline=sale_price_pipeline
    )

    st.write("### Regression Evaluation")
    # Spinner to indicate that the computation requires time
    with st.spinner("Generating Plots..."):
        # Generate and display plots for regression evaluation
        regression_evaluation_plots(
            X_train=X_train,
            y_train=y_train,
            X_test=X_test,
            y_test=y_test,
            pipeline=sale_price_pipeline,
            alpha_scatter=0.5
        )
