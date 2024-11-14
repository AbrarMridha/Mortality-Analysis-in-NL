# This file contains the data loading and cleaning methods for the analysis
# It loads the "database_var.csv" file

import pandas as pd

def load_data(file_path):
    """Load the CSV file into a DataFrame, handling encoding errors."""
    try:
        # Try reading with 'utf-8' encoding
        df = pd.read_csv(file_path, encoding='utf-8', low_memory=False)
    except UnicodeDecodeError:
        try:
            # Try reading with 'latin1' encoding
            df = pd.read_csv(file_path, encoding='latin1',low_memory=False)
        except UnicodeDecodeError:
            # Try reading with 'ISO-8859-1' encoding
            df = pd.read_csv(file_path, encoding='ISO-8859-1', low_memory=False)
    return df


def inspect_data(df):
    """Display initial data info and check for missing values."""
    print(df.head())



def clean_data(df):
    """Clean the data by filling missing values with 0"""
    return df.fillna(0)





