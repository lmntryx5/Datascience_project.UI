import streamlit as st
import pickle
import pandas as pd

st.subheader("Input the following to make predictions ")

year = st.number_input("Enter the year : ",
    min_value=0,        # Prevents negative values
    step=1,              # Moves in whole number steps
    format="%d"          # Displays as integer (no decimals# )
)

min_count = st.number_input(
    "Enter the minimum number of new HIV infections:",
    min_value=0,
    step=1,
    format="%d")

max_count = st.number_input("Enter the maximum number of new HIV infections : ",
min_value=0,
step=1,
format="%d")


with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

if st.button("Predict"):

    our_values = [year, min_count, max_count]
    our_values = pd.Series(our_values)
    test_values = our_values.values.reshape(1, -1)

    result = round(pipeline.predict(test_values)[0], 2)

    st.write(f"The model predicts {result}% increase in number of HIV cases.")


