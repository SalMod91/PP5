import streamlit as st

def page_1_summary_body():
    """
    Generates the content for the first page of the dashboard
    A quick project summary and an overview of key terms related to the project's dataset
    """

    # The following code was inspired from the Churnometer Project from Code Institute 
    st.write("## Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"### **Project Terms**\n\n"
        f"A client has inherited four properties and seeks to accurately assess and "
        f"maximize their sales prices. The focus is on ensuring that these properties "
        f"are evaluated accurately and priced competitively according to the local real "
        f"estate market conditions in Ames, Iowa, USA.\n\n"
        f"### **Project Jargons**\n\n"
        f"* **Target Variable/Target**: This is the main result or outcome that our model tries to predict.\n"
        f"* **Features/Attributes/Variables**: These words describe the characteristics "
        f"of a property and are used interchangeably to refer to the input data that "
        f"influence the target variable in our predictive model.\n"
        f"* **SalePrice**:  This is the price at which a house was sold. It is our "
        f"target variable.\n"
        f"* **Property/House**: These terms are used interchangeably to refer to the "
        f"sales records documented in the dataset.\n\n"    
        f"### **Project Dataset**\n\n"
        f"The dataset contains housing records from Ames, Iowa, detailing various "
        f"characteristics of each house. These characteristics are known as feature variables "
        f"and they include:\n"
        f"* **Floor Area**: Total floor space of the house\n\n"
        f"* **Basement**: Details about the basement area\n\n"
        f"* **Garage**: Garage size and capacity\n\n"
        f"* **Lot**: Size of the lot on which the house is built\n\n"
        f"* **Porch**: Size and type of porch\n\n"
        f"* **Wood Deck**: Details about the wood deck, if any\n\n"
        f"* **Year Built**: The year in which the house was constructed\n\n"
        f"These features help us understand and model how different aspects of a house may "
        f"influence its sale price. The dataset spans houses built between 1872 and 2010.\n\n"
        f"For a more detailed understanding of the dataset and definitions of the terms used, "
        f"please click **[HERE](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**.\n\n"
        )

    # Provide a link to the full project documentation
    st.write(
    f"For more details, please explore the **full project documentation** and "
    f"review the **[Project's README file](https://github.com/SalMod91/PP5-Heritage-Housing-Issue/blob/main/README.md)**."
        )

    # copied from README file - "Business Requirements" section
    st.success(
        f"### **Business Requirements**:\n\n"
        f"1. **Correlation Analysis**:  The client seeks to understand how various house "
        f"attributes correlate with the Sale Price. They expect the dashboard to feature "
        f"data visualizations that illustrate the relationships between these attributes "
        f"and the Sale Price.\n\n"
        f"2. **Price Prediction**: The client aims to predict the sale prices of four "
        f"inherited properties, as well as other houses in Ames, Iowa, using the "
        f"developed model.\n\n"
        f"**Performance Goals**:\n"
        f"To ensure the model meets the client's needs, we have established a performance "
        f"goal with the client that the model should achieve an R² score of at least 0.75. "
        f"This score must be maintained both on the training dataset and on the test "
        f"dataset."
        )
