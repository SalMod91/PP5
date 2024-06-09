import streamlit as st
from app_pages.multi_page import MultiPage
from app_pages.page_1_summary import page_1_summary_body
from app_pages.page_2_sale_price_study import page_2_sale_price_study_body
from app_pages.page_3_sale_price_prediction import page_3_sale_price_prediction_body
from app_pages.page_4_hypothesis_and_validation import page_4_hypothesis_validation_body

app = MultiPage(app_name= "Temporary Name")

st.write("Hello World")
st.write("This is a test to see if Streamlit works correctly")
st.write("# This is a major section")  # use markdown to create headers and sub headers
st.write("## This is subsection 1")
st.write("* Here is content for subsection 1")
st.write("## This is subsection 2")
st.write("* Here is content for subsection 2")
st.write("### This is sub-subsection 2") # you can play around by adding more sub-sections
st.info("* This is made with st.info()") # Display a text with informational style.
st.success("* This is made with st.success()") # Display a text with success style.
st.warning("* This is made with st.warning()") # Display a text with warning style.
st.error("* This is made with st.error()") # Display a text with error style.
st.write("---")  # creates a horizontal line, useful to separate the content in the page

app.app_page("Quick Project Summary", page_1_summary_body)
app.app_page("Sale Price Study", page_2_sale_price_study_body)
app.app_page("Sale Price Prediction", page_3_sale_price_prediction_body)
app.app_page("Hypothesis and Validation", page_4_hypothesis_validation_body)

app.run()
