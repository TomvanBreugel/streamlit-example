import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

def main():
    st.title("CO2 Emissie Canada")
    
    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Read CSV file
            df = pd.read_csv(uploaded_file)
            
            # Display the raw data if needed
            if st.checkbox("Show Raw Data"):
                st.write(df)
            
            # Display basic statistics
            st.subheader("Basic Statistics")
            st.write(df.describe())
            
            # Display column selection
            selected_columns = st.multiselect("Select columns to display", df.columns)
            if selected_columns:
                st.write(df[selected_columns])
                
            # Display summary statistics for selected column
            selected_column = st.selectbox("Select a column for summary statistics", df.columns)
            if selected_column:
                st.write(df[selected_column].describe())
                
            # Display a bar chart for selected column
            bar_chart_column = st.selectbox("Select a column for bar chart", df.columns)
            if bar_chart_column:
                st.bar_chart(df[CO2 Emissions(g/km)].value_counts())
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

