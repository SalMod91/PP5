import streamlit as st


def predict_sale_price(X_live, sale_price_features, sale_price_pipeline):
    """
    Predict the sale price of a house based on user-inputted features.
    """

    # Filter the data to only include the relevant features needed by the model
    X_live_sale_price = X_live.filter(sale_price_features)

    # Predict sale price using the filtered data
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

    # Convert the prediction from float to int to remove any decimal places
    sale_price_prediction = int(sale_price_prediction[0])

    return (sale_price_prediction)
