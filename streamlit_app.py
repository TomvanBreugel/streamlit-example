import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

def main():
    st.title("Excel Data Viewer")
    
    # Upload Excel file
    uploaded_file = st.file_uploader("CO2 Emissions_Canada.cvs", type=["xls","xlsx"])


