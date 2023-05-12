# Data Extraction

# TODO: Implement data extraction logic

import pandas as pd

# Read data from source system

def extract_data():
    data = pd.read_csv("source_data.csv")
    return data

# Test data extraction

def test_extract_data():
    data = extract_data()
    assert len(data) > 0
    print("Data extraction successful")