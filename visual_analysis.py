import matplotlib.pyplot as plt
from PIL.ImageColor import colormap


def plot_mortality_trend(df):
    province_data = df[df['Geography.Type']=='Province']
    province_total_death = province_data[province_data['Gender']=='Total']
    province_total_death.groupby('Year')['Total.Deaths'].sum().plot(kind='line', color='red', style='--')
    plt.title("Mortality Trend Over Time\n1990-2020")
    plt.xlabel("Year")
    plt.ylabel("Mortality Count")
    plt.ylim(3000,6000)
    plt.show()

def plot_gender_analysis(df):
    male_female_data = df[df['Gender'] != 'Total']
    male_female_data.groupby('Gender')['Total.Deaths'].sum().plot(kind='bar')
    plt.title("Mortality by Gender Over Time\n1990-2020")
    plt.xlabel("Gender")
    plt.ylabel("Mortality Count")
    plt.show()

def plot_teen_deaths_pattern(df):
    df.groupby('Year')['Deaths.Aged.Less.Than.20'].sum().plot(kind='line',style='--b')
    plt.title("Teen Deaths\n1990-2020")
    plt.xlabel("Year")
    plt.ylabel("Teen Mortality Count")
    plt.show()