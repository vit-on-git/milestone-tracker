import streamlit as st
import pandas as pd
from io import StringIO

# Streamlit app title
st.title("Personal Milestone Tracker")

# File uploader for Excel file
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Load the Excel file
    xls = pd.ExcelFile(uploaded_file)
    
    # Dropdown to select sheet name
    sheet_name = st.selectbox("Select a sheet", xls.sheet_names)
    
    # Load the selected sheet into a DataFrame
    df = xls.parse(sheet_name)
    
    # Display the raw data (optional)
    st.write("### Raw Data")
    st.write(df)
    
    # Input for month
    month = st.number_input("Enter the month (1-12) to search for", min_value=1, max_value=12, value=1)
    
    # Filter the DataFrame for dates in the specified month
    def filter_by_month(date):
        if pd.isna(date):  # Skip NaN values
            return False
        return date.month == month
    
    # Apply the filter to the relevant columns
    filtered_df = df[
        df['BirthDay'].apply(filter_by_month) |
        df['DeathDay'].apply(filter_by_month) |
        df['Anniversary'].apply(filter_by_month)
    ]
    
    # Display the filtered results
    st.write("### Filtered Results")
    st.write(filtered_df)
    
    # Download the filtered results as a CSV file
    if not filtered_df.empty:
        csv = filtered_df.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
        st.download_button(
            label="Download Filtered Results as CSV",
            data=csv,
            file_name=f"results_for_month_{month}_in_{sheet_name}.csv",
            mime="text/csv",
        )
    else:
        st.warning("No results found for the selected month.")
else:
    st.info("Please upload an Excel file to get started.")