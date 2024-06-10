import streamlit as st

def page_1_summary_body():
    """
    Generates the content for the first page of the dashboard
    A quick project summary and an overview of key terms related to the project's dataset
    """

    # The following code was inspired from the Churnometer Project from Code Institute 
    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargons**\n"
        f"* **SalePrice** is the price a house sold for and is our target variable.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents housing records from Ames, Iowa; "
        f"indicating house profile (`Floor Area, Basement, Garage, Kitchen, "
        f"Lot, Porch, Wood Deck, Year Built`) and its respective sale price for houses "
        f"built between 1872 and 2010.\n"
        f"* There are many abbreviated terms used to describe features of the houses in "
        f"the data set. For further clarification of the full dataset and explanation "
        f"of its terms you can click **[HERE](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**.\n\n"
        )

    # Provide a link to the full project documentation
    st.write(
    f"For more details, please explore the **full project documentation** and "
    f"review the **[Project's README file](https://github.com/SalMod91/PP5-Heritage-Housing-Issue/blob/main/README.md)**."
        )

    # copied from README file - "Business Requirements" section
    st.success(
        f"**The project has 2 business requirements**:\n\n"
        f"**1.**  The client is interested in discovering how house attributes correlate with "
        f"the house Sale Price. Therefore, the client expects data visualizations "
        f"of the correlated variables against Sale Price to show that.\n\n"
        f"**2.** The client is interested to predict the house sales price from their 4 "
        f"inherited houses, and any other house in Ames, Iowa. "
        )
