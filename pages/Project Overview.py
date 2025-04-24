import streamlit as st

st.title("Project Overview")

st.markdown("""
### Project Objective
To predict HIV prevalence using a machine learning model trained on WHO health data.
HIV prevalence refers to the proportion of a population that is living with HIV at a given time


### Data Source
- WHO & UNAIDS HIV statistics
- Link to Dataset : https://www.kaggle.com/datasets/imdevskp/hiv-aids-dataset?select=no_of_cases_adults_15_to_49_by_country_clean.csv
- Features: Year, estimated ranges (`Count_min`, `Count_max`), region

### Tools Used
- Python, Pandas, Scikit-learn, Streamlit, Plotly, Lasso Regression

###  Modeling Summary
- **Selected Model**: Linear Regression
- **R² Score**: 0.92
- **Features Used**: `Year`, `Count_min`, `Count_max`

### 👥 Target Users
- Public health researchers in the field 
- Students studying data science or epidemiology
- Policy planners

""")
