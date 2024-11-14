from data import load_data, inspect_data, clean_data
from visual_analysis import *

FILE_NAME = 'database_var.csv'

def main():
    # Load and inspect data
    df = load_data(FILE_NAME)

    if df is None:
        print("Data loading failed")
        return

    inspect_data()

    # Clean data
    data = clean_data(df)

    # Perform analysis and visualizations
    plot_mortality_trend(data)
    plot_gender_analysis(data)
    plot_teen_deaths_pattern(data)


if __name__ == "__main__":
    main()