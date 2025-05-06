import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_line_plot():
    # Import the data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Clean the data
    df_clean = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    # Plot the line chart
    plt.figure(figsize=(14, 6))
    plt.plot(df_clean.index, df_clean['value'], color='r', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    plt.show()

def draw_bar_plot():
    # Import the data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Clean the data
    df_clean = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    # Create a new DataFrame for grouping by year and month
    df_bar = df_clean.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group by year and month, calculate average page views
    df_bar = df_bar.groupby(['year', 'month']).mean().unstack()

    # Plot the bar chart
    plt.figure(figsize=(14, 6))
    df_bar.plot(kind='bar')
    plt.title('Average Daily Page Views, Grouped by Year and Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.show()

def draw_box_plot():
    # Import the data
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Clean the data
    df_clean = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]

    # Create a new DataFrame for grouping by year and month
    df_box_year = df_clean.copy()
    df_box_year['year'] = df_box_year.index.year

    # Create a new DataFrame for grouping by month
    df_box_month = df_clean.copy()
    df_box_month['month'] = df_box_month.index.strftime('%b')

    # Plot the box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

    sns.boxplot(x='year', y='value', data=df_box_year, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box_month, order=[
                'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.show()


draw_line_plot()
draw_bar_plot()
draw_box_plot()