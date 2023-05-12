# Data Transformation

# TODO: Implement data transformation logic to clean, filter, and enrich the extracted data

import pandas as pd

def transform_data(data):
    # TODO: Implement data transformation logic
    return data

# Test data transformation

def test_transform_data():
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    transformed_data = transform_data(data)
    assert len(transformed_data) == len(data)
    print("Data transformation successful")