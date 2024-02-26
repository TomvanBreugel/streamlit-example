import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("CSV Data Viewer")
    
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
                st.subheader(f"Bar Chart for {bar_chart_column}")
                plt.figure(figsize=(8, 6))
                sns.countplot(data=df, x=bar_chart_column)
                st.pyplot()
                
            # Display a histogram for numeric columns
            st.subheader("Histogram")
            numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
            selected_numeric_column = st.selectbox("Select a numeric column for histogram", numeric_columns)
            if selected_numeric_column:
                plt.figure(figsize=(8, 6))
                sns.histplot(df[selected_numeric_column], kde=True)
                st.pyplot()
                
            # Display a correlation heatmap
            st.subheader("Correlation Heatmap")
            plt.figure(figsize=(10, 8))
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
            st.pyplot()
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
