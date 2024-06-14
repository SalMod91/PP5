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
    st.info("""
    **Feature Importance Chart Explanation**

    The chart you see, called a "feature importance chart," helps us understand
    what characteristics of a house are most influential in determining its
    sale price.
    
    Here's how you can interpret this chart:

    - **Features**: These are different characteristics or qualities of a
    house.
    In your chart, features like the overall quality of the house, the
    living area, the year the house was built, garage area, and basement
    size are displayed.

    - **Importance**: The bars in the chart represent the importance of each
    feature—how much each characteristic contributes to the model's ability to
    predict the sale price accurately. A longer bar means the feature is more
    important in predicting the sale price.

    - **Overall Quality (OverallQual)**: This has the longest bar, indicating
    it's the most critical factor. Higher quality houses typically sell for
    more.

    - **Living Area (GrLivArea)**: The next longest bar shows that the size
    of the living areas also significantly affects the sale price.
    Larger living spaces usually increase a house’s value.

    - **Year Built (YearBuilt)**: This tells us that newer houses tend to have
    higher prices, though it’s a less significant factor than the quality or
    size.

    - **Garage Area (GarageArea)**: This shows that houses with bigger garages
    are likely to be more expensive, but it's less influential than the size
    of the house or its overall quality.

    - **Basement Size (TotalBsmtSF)**: Finally, a larger basement adds value
    to a house, but among the features shown, it impacts the price the least.
    """)

    # Display feature importance image
    st.image(feature_importance)
    st.write("---")

    st.write("## Model Evaluation")
    st.info(
        """
        **Model Evaluation Overview**

        Our model has been evaluated using various statistical metrics to
        understand its performance in predicting house sale prices.
        These metrics help us see how well the model does in both training
        (learning from the data) and testing (performing
        with new, unseen data) phases.
        Here's a breakdown of what each metric means:

        - **R2 Score**: Explains the proportion of variance in the dependent
        variable that is predictable from the independent variables.
        Closer to 1 is ideal.

        - **Mean Absolute Error**: The average absolute difference between the
        observed actual outcomes and the predictions by the model.

        - **Mean Squared Error**: Similar to MAE but squares the differences;
        it punishes larger errors more severely.

        - **Root Mean Squared Error**: The square root of MSE, providing error
        terms in the same units as the target variable, making it slightly
        more interpretable than MSE.
        """)

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

    st.write("---")
    st.write("## Conclusions")
    st.write("""
        ### Model Performance Summary

        **Selected Standard Regression Model Overview**:
        The selected standard regression model, equipped with the best
        features, has been configured to predict the sale price of homes.
        Here's an overview of its performance:

        **Strong Training Performance**:
        - The model demonstrates outstanding predictive accuracy within
        the training dataset, achieving a high R2 score of 0.934.
        This indicates a strong fit to the known data.

        **Performance on Test Data**:
        - A decline in the R2 score to 0.844 on the test set suggests that
        while the model remains robust, it naturally experiences a decrease in
        performance when applied to new, unseen data.

        - This decrease is typical in predictive modeling and reflects the
        challenges of generalizing from training data to real-world scenarios.

        **Error Metrics Analysis (MAE, MSE, RMSE)**:
        - The observed disparities between training and testing performance,
        particularly noted in the error metrics, hint at overfitting.
        This occurs when a model learns the training data too intricately,
        capturing its noise and anomalies, which hinders its ability to
        generalize effectively.

        - Despite signs of overfitting, the model still maintains considerable
        generalization capability with an R2 score of 0.844 on the test set,
        illustrating its robustness.

        **Summary**:
        - The current regression model showcases potent predictive strength
        with optimally selected features.
        However, it could benefit from implementing strategies to mitigate
        overfitting, thus enhancing its accuracy and reliability on unseen
        data.

        - The model has successfully met the performance target of achieving
        an R2 score of at least 0.75 in both the training and test datasets,
        affirming its efficacy in practical applications.
    """)
