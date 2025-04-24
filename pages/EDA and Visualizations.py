import streamlit as st

st.set_page_config(page_title="EDA Insights", layout="wide")
st.title("Exploratory Data Analysis (EDA) Insights")
st.markdown("""
This page presents detailed insights from the exploratory data analysis (EDA) phase of the HIV prevalence dataset.
These findings are based on our original notebook: `Data_Science_Project_.ipynb`.
""")

# Dataset Overview
st.header("Dataset Overview")
st.markdown("""
- **Total records**: 680  
- **Years covered**: 2000 to 2018  
- **Countries**: 170  
- **WHO Regions**: 6  
- **Key Variables**:  
  - `Country`, `Year`, `Count_min`, `Count_median`, `Count_max`, `WHO Region`  
  - `Count`: raw format like "0.1[0.1–0.1]" (not used for modeling)
""")

# Missing Data
st.header("Missing Data Handling")
st.markdown("""
- Missing Values were removed before model training
- A heatmap was used to visualize missing values
""")
st.code("sns.heatmap(df.isnull(), cbar=False, cmap='YlGnBu')", language='python')

# Categorical Distribution
st.header("WHO Region & Country Distribution")
st.markdown("""
- `Europe` had the most entries (≈200 records)  
- Top 10 most frequent countries were displayed  
""")
st.code("df['WHO Region'].value_counts()\ndf['Country'].value_counts().head(10)", language='python')

# Numeric Distributions
st.header("Prevalence Value Distributions")
st.markdown("""
Histograms with KDE were plotted for:
- `Count_min`
- `Count_median`
- `Count_max`

This helped detect outliers and shape of the distributions.
""")
st.code("""
for col in ['Count_min', 'Count_median', 'Count_max']:
    sns.histplot(df[col], bins=20, kde=True)
""", language='python')

# Correlation and Range
st.header("Correlation & Range Analysis")
st.markdown("""
- `Count_min` and `Count_max` had a **very strong correlation (≈0.99)** with `Count_median`
- A new column `Count_range = Count_max - Count_min` was created
- Countries with the largest ranges were identified
""")
st.code("""
df['Count_range'] = df['Count_max'] - df['Count_min']
df[['Country', 'Count_range']].sort_values(by='Count_range', ascending=False).head()
""", language='python')

# Relative Range
st.markdown("""
A relative percentage range column was also added:

> `(Count_max - Count_min) / Count_median * 100`
""")
st.code("df['range_percent'] = (df['Count_max'] - df['Count_min']) / df['Count_median'] * 100", language='python')

# Time Trends
st.header("Time Trends by WHO Region")
st.markdown("""
HIV prevalence was tracked across time by WHO region to observe trends over the years.
""")
st.code("df.groupby(['Year', 'WHO Region'])['Count_median'].sum().unstack().plot()", language='python')

# Global Burden Share
st.header("Global Share of HIV Burden")
st.markdown("""
We calculated each country’s contribution to the global prevalence total:
""")
st.code("""
total_global = df['Count_median'].sum()
df['global_share_percent'] = (df['Count_median'] / total_global) * 10
""", language='python')

# Feature Selection
st.header("Feature Selection Summary")
st.markdown("""
Using **Lasso Regression**, the most relevant features selected for modeling were:
- `Count_min`
- `Count_max`
- `Year`

The following were not used for prediction :
- `Country`
- `WHO Region`
""")

# Final Takeaways
st.header("Final Takeaways")
st.markdown("""
| Insight                          | Impact                                  |
|----------------------------------|-----------------------------------------|
| Strong correlation in estimates | Used for accurate predictions           |
| Categorical features weak       | Removed for simplicity                  |
| Missing data handled cleanly    | Ensured reliable model inputs           |
| Region & time trends observed   | Support for visual storytelling         |
| R² = 0.92                        | Strong model performance                |
""")

st.success("These findings informed the feature selection, modeling, and visual design choices throughout the app.")
