# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Business Overview
The primary objective of this project is to develop a data-driven web application that enables the client to accurately predict house sale prices based on various house attributes and provides insightful visualizations of how these attributes correlate with sale prices. This will aid the client in making informed decisions regarding the sale of four inherited properties and any future real estate investments in Ames, Iowa.

## CRISP-DM
### What is CRISP-DM?

CRISP-DM, which stands for Cross-Industry Standard Process for Data Mining, is a widely adopted methodology for data mining projects. It provides a structured approach to planning and executing data mining tasks.

The CRISP-DM framework consists of six phases:

1. **Business Understanding**: This initial phase focuses on understanding the project objectives and requirements from a business perspective, then converting this knowledge into a data mining problem definition and a preliminary plan.

2. **Data Understanding**: This phase starts with data collection and proceeds with activities aimed at familiarizing with the data, identifying data quality issues and discovering initial insights.

3. **Data Preparation**: The data is prepared for modeling by performing tasks such as data cleaning and formatting data as necessary.

4. **Modeling**: Various modeling techniques are selected and applied. During this phase, models are calibrated to optimal parameter settings and tested to ensure they are appropriate for the data.

5. **Evaluation**: The model or models are thoroughly evaluated and reviewed to ensure they effectively meet the initial business objectives set out in the first phase.

6. **Deployment**: The completion of the process involves deploying the data mining solution to the business.

### CRISP-DM Workflow
The development followed the Cross Industry Standard Process for Data Mining (CRISP-DM), organized into distinct phases and can be found [HERE](https://github.com/SalMod91/PP5-Heritage-Housing-Issue/issues?q=is%3Aissue+is%3Aopen):

- **Epic 1: Business Understanding**:
    
    This stage involved extensive discussions with the client to understand their expectations and develop acceptance criteria, which are detailed in the [Business Requirements](#business-requirements) section below.

- **Epic 2: Data Understanding**: 
    
    This stage was dedicated to conducting an exploratory study to identify the factors influencing the sale price, using raw data to avoid introducing biases through premature data preparation.
    
    This approach was chosen to ensure that the insights derived from the unaltered data were genuine and reflective of the true dynamics present in the dataset.
    
    This phase directly addresses and fulfills the first business requirement, as detailed in the [Business Requirements](#business-requirements), which was performed in the Sale Price Study Notebook.

- **Epic 3: Data Preparation**:

    This critical step involved cleaning and imputing data, conducting feature engineering like transformations or scaling, and reformatting data as needed.
    
    These tasks  were performed in the Data Cleaning and Feature Engineering Notebooks.

- **Epic 4: Modeling**:

    This phase focused on selecting modeling algorithms and splitting the data into training and testing sets.
    
    The training set was used to validate various algorithms and tune them through hyperparameter optimization and was performed in the Modeling and Evaluation Notebook.

- **Epic 5: Evaluation**:

    The test set was used to evaluate model performance, ensuring alignment with the business acceptance criteria.

    The evaluation was performed in the Modeling and Evaluation Notebook.

- **Epic 6: Deployment**:

    A Streamlit app was developed to meet the business requirements established with the client.
    
    The app was deployed on Heroku, with the process described in the [Deployment](#deployment) section.

### Agile Development
To effectively manage the CRISP-DM workflow for my project, I've adopted Agile development practices, as they are both iterative and flexible frameworks that can effectively complement each other.

I've aligned each stage of the CRISP-DM process with an Agile epic, breaking down the complex tasks into manageable user stories.

This structure has enabled me to adaptively add tasks as the project evolved.

Link to Epics: [Epics](https://github.com/SalMod91/PP5-Heritage-Housing-Issue/issues?q=is%3Aissue+is%3Aopen)

Link to Kanban Board: [User Stories](https://github.com/users/SalMod91/projects/8)

## Business Requirements

- Data Visualization Requirement: <br>
    The client requires a dashboard that displays visualizations of house attributes correlated with sale prices to understand market trends and factors influencing house values in Ames, Iowa.

- Predictive Analysis Requirement: <br>
    The client needs a robust predictive model integrated within the dashboard that can forecast the sale prices of her four inherited houses and any additional houses in Ames. <br>This model should use historical data and house attributes to generate predictions.

### Succes Metrics
**Model Performance:** <br>
    Achievement of an R2 score of at least 0.75 on both the training and testing datasets, indicating strong predictive accuracy of the model.

**Variable Correlation Analysis:** <br>
    Completion of a comprehensive study identifying and visualizing the most relevant variables that are correlated with the sale price. This includes clear documentation and presentations of these correlations through the dashboard to aid in understanding how different house attributes impact sale prices in Ames, Iowa.

**Predictive Capability:** <br>
    Successful implementation of the predictive model within the dashboard that can accurately forecast sale prices for the four inherited properties, as well as for any other house in Ames. The predictions should consistently align with actual market prices, demonstrating the model's effectiveness.

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|


## Hypothesis and how to validate?

1. **Hypothesis**: There is a positive correlation between the size-related features of a property and its sale price.
    - **Validation Method**: Conduct a correlation analysis to determine the strength and direction of the relationship between property size features and sale prices.

2. **Hypothesis**: The year a property was built is positively correlated with its sale price.
    - **Validation Method**: Perform a correlation analysis to assess the relationship between the year of construction and the sale price of properties.

3. **Hypothesis**: Based on the identified features, it is possible to predict sale prices with an accuracy yielding an R² score of at least 0.75.
    - **Validation Method**: Develop a regression model using the identified features to predict property sale prices. Validate the model by calculating the R² score on a test dataset to ensure the prediction accuracy meets or exceeds 0.75.

## Mapping the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Correlation Study and Data Visualization

- **Objective**: To analyze the data related to house sales to uncover how various house attributes correlate with the sale price.

- **Tasks**:

    - **Data Inspection**: Review and inspect the dataset containing house records to ensure a comprehensive understanding of the available data.

    - **Correlation Analysis**: Perform both Pearson and Spearman correlation studies to identify the relationships between various variables and the sale price.

    - **Data Visualization**: Create visual plots of key variables against the sale price to derive actionable insights and visually represent how house attributes impact sale prices.

- **User Stories**:

    - As a client, I want to review the data related to house records to explore how the house attributes influence the sale price.

    - As a client, I want to visually map the main variables against the sale price to better understand and visualize the impact of different attributes on house pricing.

### Business Requirement 2: Predictive Modeling and Performance Evaluation

- **Objective**: To develop predictive models that accurately estimate house values and evaluate their performance.

- **Tasks**:
    - **Model Development**: Construct a regression model to predict the sale price as the dependent variable.
    - **Visualization**: Create visual representations to compare the predictions of the train and test sets against actual sale prices.
    - **Model Evaluation**: Conduct regression analysis to determine the R² Score and Mean Absolute Error, ensuring the model's accuracy and reliability.

- **User Stories**:
    - As a client, I want to predict the sale price of my four inherited properties using a machine learning model.
    - As a client, I want the flexibility of predicting the sale price of any other home in Ames, Iowa.

## ML Business Case

### Machine Learning Model Development for Predicting House Sale Prices

**Project Objective**:


This project aims to develop a machine learning (ML) model to predict the sale price, in dollars, of homes in Ames, Iowa. The target variable is a continuous number, indicating the sale price. The focus is on a regression model, which is supervised and uni-dimensional, to offer a robust tool for predicting the sale prices of homes, particularly for a client's inherited properties.

**Success Criteria**:

- **Correlation Study**: Deliver a comprehensive analysis identifying key variables that significantly correlate with the sale price. This study will help in understanding which features impact the sale price most.

- **Predictive Accuracy**: Develop a regression model capable of predicting the sale price with high reliability. The model should achieve an R² score of at least 0.75 on both training and testing datasets, ensuring it can accurately predict the sale prices of the four specific inherited properties and other homes in the region.

**Model Selection**:

- Based on the characteristics of the data and the nature of the target variable (sale price), a regression model is suggested.

Client Benefits:

- **Maximizing Investment Returns**: By accurately predicting the sale prices, the client can make informed decisions regarding when and at what price to sell the inherited properties, potentially maximizing their investment returns.
    
- **Strategic Planning**: Reliable sale price predictions will aid the client in strategic planning and management of property assets.

**Model Inputs and Outputs**:

- **Inputs**: The model will utilize a range of house attributes such as size, age and conditions inputs to predict the sale price.

- **Outputs**: The primary output from the model will be the predicted sale price of a home as a continous value in dollars.

## Dashboard Design

### Dashboard Expectations
**Dashboard Overview**:

The dashboard will serve as a multifunctional platform, presenting detailed insights, predictions, and analyses related to house sale prices. It will include the following key pages:

### Page 1: Project summary

- **Overview**: Provide a concise summary of the project.
- **Project Terms and Jargon**: Define specific terminology used throughout the project.
- **Dataset Prescription**: Outline the characteristics and scope of the project dataset.
- **Business Requirements**: Detail the client's needs and expectations from the project.

### Page 2: Sale Price Study

- **Purpose**: Address Business Requirement 1 by identifying and displaying key features that strongly correlate with house sale prices.
- **Correlation Analysis**: Discuss the methodologies used for the correlation study and their findings.
- **Data Visualization**: Offer visual representations of the data to highlight significant correlations.

### Page 3: Sale Price Predictions
- **Objective**: Fulfill Business Requirement 2 by showcasing predictions for the four inherited properties.
- **Prediction Display**: List the attributes of the four properties along with their predicted sale prices.
- **Real-Time Prediction Widget**: Include an interactive input widget that allows users to input real-time data to receive instant sale price predictions.

### Page 4: Hypothesis Testing and Validation
- **List of Hypotheses**: Enumerate the project hypotheses.
- **Validation Process**: Explain how each hypothesis was tested and validated throughout the project.

### Page 5: Machine Learning Model Analysis
- **Model Overview**: Describe the machine learning pipeline used for training the model.
- **Feature Significance**: Discuss the importance of various features within the model.
- **Performance Analysis**: Provide an evaluation of the model’s performance, including metrics and insights.

## Unfixed Bugs

- Some logs are showing warnings related to the use of deprecated versions of libraries or methods.
- When navigating between pages in the Streamlit dashboard, the state of checkboxes does not reset as expected.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

