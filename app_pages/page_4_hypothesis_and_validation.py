import streamlit as st


def page_4_hypothesis_validation_body():

    st.write("## Hypothesis and Validation")

    # Based on the findings in Notebook 02: Sale Price Study
    # Property Size Hypothesis
    st.write("### Property Size Hypothesis")
    st.success(
        "We hypothesize that features relating to the size of a property "
        "are positively correlated to sale price.\n\n"
        "**Accept hypothesis:** The analysis shows "
        "a strong positive correlation "
        "between property size and sale price, as demonstrated by:\n\n"
        "- **1stFlrSF**, **GarageArea**, **GrLivArea**, and **TotalBsmtSF**"
        " have strong positive correlations with SalePrice.\n"
        "- **GrLivArea** (Living Area) is significantly positively "
        "correlated, indicating larger homes tend to have higher values.\n"
        "- Both garage and basement sizes (**GarageArea** and **TotalBsmtSF**)"
        " are significant predictors, emphasizing that usable space is"
        " a crucial factor in property valuation."
    )

    # Year Built Hypothesis
    st.write("### Year Built Hypothesis")
    st.success(
        "We hypothesize that the newer properties,"
        " particularly the year built, "
        "are positively correlated with sale price.\n\n"
        "**Accept hypothesis:** There is a noticeable"
        " positive correlation between "
        "the year properties were built and their sale prices."
        " This correlation is apparent "
        "from the data and further supported by the fact that"
        " properties listed as remodeled "
        "at the time of construction also fetch higher prices,"
        " impacting the correlation between "
        "**Year Built** and the sale price."
    )

    # Kitchen Quality Hypothesis
    st.write("### Kitchen Quality Hypothesis")
    st.info(
        "We hypothesize that kitchen quality has a strong positive"
        " correlation with sale price.\n\n"
        "**Modify hypothesis:** While kitchen quality "
        "(**KitchenQual**) strongly correlates with **SalePrice**, "
        "it mirrors overall quality closely."
        " This suggests that overall property quality may be a more efficient "
        "predictor in modeling, with **OverallQual** being the critical"
        " predictor as it encapsulates broader aspects "
        "of property appeal."
    )

    # Sale Price Prediction Hypothesis
    st.write("### Sale Price Prediction Hypothesis")
    st.success(
        "We hypothesize that we are able to predict sale prices accurately"
        " based on the identified features "
        "and achieve an R² score of 0.75.\n\n"
        "**Accept hypothesis:** The model successfully predicts sale prices"
        " with high accuracy, achieving an R² score of 0.934 on the training"
        " set and 0.844 on the test set. "
        "These results reflect strong correlations and insights gained"
        " from detailed data analysis, including predictive "
        "modeling techniques like regression analysis."
    )

    # Additional insights from Sale Price Study
    st.write("### Insights from Sale Price Study")
    st.write(
        "**Analysis Insights**:\n"
        "- **Overall Quality**: Shows the most robust correlation with"
        " Sale Price, suggesting it as the most critical predictor. "
        "Houses with higher overall quality are consistently priced higher.\n"
        "- **Living Area**: There is a strong positive correlation between"
        " living area and Sale Price, indicating that larger"
        " homes tend to have higher values.\n"
        "- **Garage and Basement Sizes**: Both are significant predictors"
        " of Sale Price, indicating that usable space greatly"
        " influences the sale price.\n"
        "- **Year Built and Remodeled**: Newer homes typically have a higher"
        " sale price. There's a significant overlap in the years built and"
        " remodeled, suggesting properties are often listed as remodeled"
        " at the time of construction.\n"
        "- **Kitchen Quality**: Strongly correlates with Sale Price but also"
        " closely mirrors overall quality, suggesting that focusing on "
        "overall quality might suffice in predictive modeling."
    )
