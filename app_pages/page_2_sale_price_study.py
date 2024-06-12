import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import ppscore as pps

def page_2_sale_price_study_body():
    """
    Generates the content for the second page of the dashboard
    It loads data, displays business requirements, and visualizes correlations and PPS.
    """

    df = load_house_data()

    # Define variables of interest for the bivariate analysis
    variables_to_study = {
        'OverallQual': 'Rating 1-10',
        'GrLivArea': 'Square Feet',
        'GarageArea': 'Square Feet',
        'TotalBsmtSF': 'Square Feet',
        'YearBuilt': 'Year',
        '1stFlrSF': 'Square Feet',
        'YearRemodAdd': 'Year',
    }

    # Header
    st.write("## Sale Price Study")

    # Business requirements information
    st.success(
        f"#### Business Requirement 1\n\n"
        f"* The client is interested in discovering how the house attributes correlate "
        f"with the **Sale Price**. Therefore, the client expects data visualizations"
        f" of the correlated variables against the sale price to show that."
    )

    # Checkbox to show dataset details
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

    # Correlation and PPS studies explained
    st.write("## Correlation Study")
    st.write(
        "A correlation analysis was performed using both Pearson and Spearman methods, "
        f"identifying the most significant features for predicting Sale Price as:\n\n "
        "- **Overall Quality**\n"
        "- **Ground Living Area**\n"
        "- **1st Floor Area**\n"
        "- **Garage Area**\n"
        "- **Total Basement Area**\n"
        "- **Year Built**\n"
        "- **Year Remodeled**\n\n"
        "The features listed above exhibit strong linear and monotonic relationships with Sale Price, "
        "signifying that:\n"
        "- The sale price is higher for homes with higher overall quality.\n"
        "- The sale price increases with the size of the house, indicating larger houses tend to sell for more.\n"
        "- The sale price is higher for recently built houses.\n\n"
        "Visualizations below further illustrate these correlations through detailed plots "
        "between the identified features and the target variable.\n\n"
    )

    # Display a warning message about potential delays
    st.warning(
        "**Note**: Due to the heavy computation requirements, the visualizations may "
        "take a few seconds to display."
    )

    # Pearson correlation explanation and visualization
    st.info(
        "### Pearson's Correlation Study\n"
        "Pearson’s correlation coefficient measures the strength of a linear "
        "association between two continuous variables, providing a value between -1 and 1.\n\n "
        "Here's what the values indicate:\n"
        "- A coefficient of 1 implies a perfect positive linear relationship, where one "
        "variable increases in direct proportion to the other.\n"
        "- A coefficient of -1 implies a perfect negative linear relationship, where one "
        "variable increases as the other decreases.\n"
        "- A coefficient of 0 indicates no linear correlation, suggesting no linear "
        "dependence between the variables.\n\n"
        "Below, there is an illustration through a heatmap and barplots showing "
        "the features most strongly correlated to the Sale Price."
    )

    # Checkbox to view Pearson correlation
    if st.checkbox("Pearson Correlation"):
        calculate_corr_pearson(df)
        plot_correlation_bar(df, method="pearson")


    # Spearman correlation explanation and visualization
    st.info(
        "### Spearman's Correlation Study\n"
        "Spearman’s correlation coefficient evaluates the monotonic relationship "
        "between two continuous or ordinal variables. It provides a value between -1 and 1, "
        "indicating the strength and direction of the association.\n\n"
        "Here's what the values indicate:\n"
        "- A coefficient of 1 signifies a perfect positive monotonic relationship, where "
        "the ranking of one variable increases with the ranking of the other.\n"
        "- A coefficient of -1 signifies a perfect negative monotonic relationship, where "
        "the ranking of one variable decreases as the ranking of the other increases.\n"
        "- A coefficient of 0 indicates no monotonic correlation, suggesting that the "
        "variables do not maintain a consistent direction in their relationship.\n\n"
        "Below, there is an illustration through a heatmap and barplots showing "
        "the features most strongly correlated to the Sale Price."
    )

    # Checkbox to view Spearman correlation
    if st.checkbox("Spearman Correlation"):
        calculate_corr_spearman(df)
        plot_correlation_bar(df, method="spearman")
    
    # PPS heatmap explanation and visualization
    st.info(
        "### Predictive Power Score (PPS) Heatmap\n"
        "The PPS heatmap is a visual tool that helps identify which features are good predictors "
        "for a specific variable. To use this heatmap effectively, follow these steps:\n\n"
        "- **Locate the Target Variable**: Find the variable you are interested in on the Y-axis of the heatmap. "
        "This is the variable for which you want to identify good predictors.\n"
        "- **Analyze Predictors**: Look across the corresponding row on the X-axis to see which features "
        "are good predictors of the target variable. The heatmap cells are colored based on the PPS score: "
        "darker colors typically indicate stronger predictive power.\n\n"
        "**Rule of Thumb for Good Predictive Power**:\n"
        "- A PPS Score above 0.2 is often considered to have moderate predictive power, indicating "
        "that the variable contributes valuable information that might be significant in predictive models.\n"
        "- A PPS Score above 0.5 generally indicates strong predictive power, suggesting a substantial "
        "influence of the predictor on the target variable.\n\n"
        "**Note on Diagonal Entries in Heatmaps**:\n\n"
        "The diagonal cells in a PPS heatmap, where a variable intersects with itself, "
        "always score 1 because a variable perfectly predicts itself. These entries should be ignored "
        "as they do not provide insights into the predictive relationships between different features.\n\n"
        "Below, an illustration through a heatmap displays "
        "the variables with the highest Predictive Power Scores, highlighting key relationships both "
        "with the Sale Price and among the features themselves.\n\n"
    )

    # Checkbox to view PPS
    if st.checkbox("PPS"):
        calculate_pps(df)

    st.write(
        """
        ## Bivariate Analysis

        Bivariate analysis involves examining the relationships between two variables. 
        To better understand the positive relationships between features most correlated 
        with the sale price, we will utilize regression plots. 
        """
    )
    
    st.info(
        """
        **About Regression Plots**:
        Regression plots show the relationship between two variables with data points and a line of best fit. 
        This line helps us see the trend and understand how changes in one variable could influence the other. 
        They are especially useful for seeing how features linked to sale price impact its values.
        """
    )

    if st.checkbox("Bivariate Analysis"):
        plot_regression(df, variables_to_study)


# Section for functions
def heatmap_corr(df, threshold, figsize=(20,12), font_annot=8):
    """
    Generates a heatmap to visualize the correlations of the DataFrame.
    """
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                    linewidth=0.5)
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    """
    Generates a heatmap for Predictive Power Scores (PPS) of the DataFrame.
    """
    if len(df.columns) > 1:

      mask = np.zeros_like(df, dtype=np.bool)
      mask[abs(df) < threshold] = True

      fig, ax = plt.subplots(figsize=figsize)
      ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                       mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                       linewidth=0.05,linecolor='grey')

      plt.ylim(len(df.columns),0)
      st.pyplot(fig)

def calculate_pps(df):
    """
    Calculates the Predictive Power Score (PPS) matrix and displays it using a heatmap.
    """
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T
    heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(12,10), font_annot=10)


def calculate_corr_pearson(df):
    """
    Calculates the Pearson Correlation Coefficient and displays it using a heatmap.
    """
    df_corr_pearson = df.corr(method="pearson")
    heatmap_corr(df=df_corr_pearson, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def calculate_corr_spearman(df):
    """
    Calculates the Spearman Correlation Coefficient and displays it using a heatmap.
    """
    df_corr_spearman = df.corr(method="spearman")
    heatmap_corr(df=df_corr_spearman, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def plot_correlation_bar(df, method='pearson'):
    """
    Plots a bar chart of the strongest correlations with Sale Price using the specified correlation method.
    """
    df_corr = df.corr(method=method)['SalePrice'].drop('SalePrice')

    threshold = 0.5
    significant_corrs = df_corr[abs(df_corr) > threshold].sort_values(ascending=False)

    plt.figure(figsize=(12, 10))
    sns.barplot(x=significant_corrs.values, y=significant_corrs.index, palette="viridis")
    plt.title(f'Top Correlations with Sale Price using {method.title()} Correlation')
    plt.xlabel('Correlation Coefficient')
    plt.ylabel('Features')
    
    st.pyplot(plt)

def plot_regression(df, variables_to_study):
    """
    Plots regression plots for specified variables against the Sale Price
    """
    for variable, unit in variables_to_study.items():
        plt.figure(figsize=(10, 6))
        sns.regplot(x=variable, y='SalePrice', data=df, line_kws={"color": "red"}, ci=None)
        sns.set_style("whitegrid")
        plt.title(f'Sale Price vs. {variable}')
        plt.xlabel(f'{variable} ({unit})')
        plt.ylabel('Sale Price ($)')
        plt.grid(True)

        st.pyplot(plt)
