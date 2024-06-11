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

        st.write(
        """
        ### Data Dictionary:

        Below is a detailed explanation of each variable in our dataset.

        - **1stFlrSF**: First Floor square feet
        - **2ndFlrSF**: Second floor square feet
        - **BedroomAbvGr**: Bedrooms above grade (does NOT include basement bedrooms)
        - **BsmtExposure**: Walkout or garden level walls
            - *Gd*: Good Exposure
            - *Av*: Average Exposure
            - *Mn*: Minimum Exposure
            - *No*: No Exposure
            - *None*: No Basement
        - **BsmtFinSF1**: Type 1 finished square feet
        - **BsmtFinType1**: Rating of basement finished area
            - *GLQ*: Good Living Quarters
            - *ALQ*: Average Living Quarters
            - *BLQ*: Below Average Living Quarters
            - *Rec*: Average Rec Room
            - *LwQ*: Low Quality
            - *Unf*: Unfinished
            - *None*: No Basement
        - **BsmtUnfSF**: Unfinished square feet of basement area
        - **EnclosedPorch**: Enclosed porch area in square feet
        - **GarageArea**: Size of garage in square feet
        - **GarageFinish**: Interior finish of the garage
            - *Fin*: Finished
            - *RFn*: Rough Finished
            - *Unf*: Unfinished
            - *None*: No Garage
        - **GarageYrBlt**: Year garage was built
        - **GrLivArea**: Above grade (ground) living area square feet
        - **TotalBsmtSF**: Total square feet of basement area
        - **KitchenQual**: Kitchen quality
            - *Ex*: Excellent
            - *Gd*: Good
            - *TA*: Typical/Average
            - *Fa*: Fair
            - *Po*: Poor
        - **LotArea**: Lot size in square feet
        - **LotFrontage**: Linear feet of street connected to property
        - **MasVnrArea**: Masonry veneer area in square feet
        - **OpenPorchSF**: Open porch area in square feet
        - **OverallCond**: Rates the overall condition of the house
            - *10*: Very Excellent
            - *9*: Excellent
            - *8*: Very Good
            - *7*: Good
            - *6*: Above Average
            - *5*: Average
            - *4*: Below Average
            - *3*: Fair
            - *2*: Poor
            - *1*: Very Poor
        - **OverallQual**: Rates the overall material and finish of the house
            - *10*: Very Excellent
            - *9*: Excellent
            - *8*: Very Good
            - *7*: Good
            - *6*: Above Average
            - *5*: Average
            - *4*: Below Average
            - *3*: Fair
            - *2*: Poor
            - *1*: Very Poor
        - **WoodDeckSF**: Wood deck area in square feet
        - **YearBuilt**: Original construction date
        - **YearRemodAdd**: Remodel date (same as construction date if no remodelling or additions)
        - **SalePrice**: Sale Price
        """
    )
