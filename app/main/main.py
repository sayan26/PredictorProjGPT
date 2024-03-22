import streamlit as st
import pandas as pd
import reportPrompt

st.title("Performance Data Extractor")

st.sidebar.header("Input Text")
input_text = st.sidebar.text_area("Enter your text here:")

output_data = pd.DataFrame(columns=["Measure", "Value"])


def extract_performance_data():
    # Replace this with your own logic to extract data from the input text
    # For demonstration purposes, we'll assume the data is in a specific format
    data = {
        "Measure": ["Response time", "Wait time", "Pacing", "CPU Utilization", "Memory Consumption", "Error %"],
        "Value": ["", "", "", "", "", ""]
    }
    return pd.DataFrame(data)


if st.sidebar.button("Extract"):
    if input_text:
        extracted_data = reportPrompt.extract_performance_data(input_text)
        if not extracted_data.empty:
            output_data = extracted_data

st.header("Extracted Data")
st.table(output_data)

st.sidebar.markdown("#### Instructions")
st.sidebar.markdown("1. Enter the text in the left sidebar.")
st.sidebar.markdown("2. Click the 'Extract' button to extract performance data.")
