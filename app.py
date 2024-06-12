import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_1_summary import page_1_summary_body
from app_pages.page_2_sale_price_study import page_2_sale_price_study_body
from app_pages.page_3_sale_price_prediction import page_3_sale_price_prediction_body
from app_pages.page_4_hypothesis_and_validation import page_4_hypothesis_validation_body
from app_pages.page_5_ml_model import page_5_ml_model_body

app = MultiPage(app_name= "Housing Sale Price Predictor")

app.app_page("Quick Project Summary", page_1_summary_body)
app.app_page("Sale Price Study", page_2_sale_price_study_body)
app.app_page("Sale Price Prediction", page_3_sale_price_prediction_body)
app.app_page("Hypothesis and Validation", page_4_hypothesis_validation_body)
app.app_page("Machine Learning Model", page_5_ml_model_body)

app.run()
