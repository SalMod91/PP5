import streamlit as st

def page_1_summary_body():
    """
    Generates the content for the first page of the dashboard
    A quick project summary and an overview of key terms related to the project's dataset
    """

    # The following code was inspired from the Churnometer Project from Code Institute 
    st.write("## Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info("""
    ### **Project Terms**

    A client has inherited four properties and seeks to accurately assess and maximize their sales prices. The focus is on ensuring that these properties are evaluated accurately and priced competitively according to the local real estate market conditions in Ames, Iowa, USA.

    ### **Project Jargons**

    * **Target Variable/Target**: This is the main result or outcome that our model tries to predict.
    * **Features/Attributes/Variables**: These words describe the characteristics of a property and are used interchangeably to refer to the input data that influence the target variable in our predictive model.
    * **SalePrice**:  This is the price at which a house was sold. It is our target variable.
    * **Property/House**: These terms are used interchangeably to refer to the sales records documented in the dataset.

    ### **Project Dataset**

    The dataset contains housing records from Ames, Iowa, detailing various characteristics of each house. These characteristics are known as feature variables and they include:
    * **Floor Area**: Total floor space of the house
    * **Basement**: Details about the basement area
    * **Garage**: Garage size and capacity
    * **Lot**: Size of the lot on which the house is built
    * **Porch**: Size and type of porch
    * **Wood Deck**: Details about the wood deck, if any
    * **Year Built**: The year in which the house was constructed

    These features help us understand and model how different aspects of a house may influence its sale price. The dataset spans houses built between 1872 and 2010.

    For a more detailed understanding of the dataset and definitions of the terms used, please click **[HERE](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**.
    """)

    # Provide a link to the full project documentation
    st.write(
    f"For more details, please explore the **full project documentation** and "
    f"review the **[Project's README file](https://github.com/SalMod91/PP5-Heritage-Housing-Issue/blob/main/README.md)**."
        )

    # copied from README file - "Business Requirements" section
    st.success("""
    ### **Business Requirements**:

    1. **Correlation Analysis**: The client seeks to understand how various house attributes correlate with the Sale Price. They expect the dashboard to feature data visualizations that illustrate the relationships between these attributes and the Sale Price.

    2. **Price Prediction**: The client aims to predict the sale prices of four inherited properties, as well as other houses in Ames, Iowa, using the developed model.

    **Performance Goals**:
    To ensure the model meets the client's needs, we have established a performance goal with the client that the model should achieve an R² score of at least 0.75. This score must be maintained both on the training dataset and on the test dataset.
    """)
