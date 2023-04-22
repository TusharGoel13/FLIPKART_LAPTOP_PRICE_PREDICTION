import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import re

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "laptop_details_modified.csv")

st.set_page_config(page_title='Laptop Data Visualization')

df = pd.read_csv(DATA_PATH)

st.header(":violet[Charts]")

columns = ['Rating', 'MRP', 'Brand', 'Processor', 'RAM Type', 'RAM Capacity (GB)', 'HDD Storage', 'SSD Storage', 'Operating System', 'Display Size', 'Warranty']
selected_column = st.selectbox('Select Column', columns)

def plot_boxplot(x, y, xlabel, title):
    plt.figure(figsize=(12, 8))
    sns.boxplot(x=x, y=y.dropna())
    plt.xlabel(xlabel)
    plt.title(title)
    plt.xticks(rotation=45)
    st.pyplot(plt)

def plot_countplot(x, data, xlabel, ylabel, title):
    sns.set(style="darkgrid")
    plt.figure(figsize=(12, 8))
    sns.countplot(x=x, data=data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

if selected_column:
    if selected_column == 'Rating':
        plot_countplot('Rating', df, 'Rating', 'Frequency', 'Distribution of Ratings')
    elif selected_column == 'MRP':
        plot_boxplot(df['Brand'], df['MRP'], 'Brand', 'Distribution of MRP')
    elif selected_column == 'Brand':
        plot_countplot('Brand', df, 'Brand', 'Frequency', 'Proportion of Brands')
    elif selected_column == 'Processor':
        plot_countplot('Processor', df, 'Processor', 'Frequency', 'Distribution of Processor Types')
    elif selected_column == 'RAM Type':
        plot_countplot('RAM Type', df, 'RAM Type', 'Frequency', 'Distribution of RAM Types')
    elif selected_column == 'RAM Capacity (GB)':
        plot_countplot('RAM Capacity (GB)', df, 'RAM Capacity (GB)', 'Frequency', 'Distribution of RAM Capacities')
    elif selected_column == 'HDD Storage':
        plot_countplot('HDD Storage', df, 'HDD Storage (GB)', 'Frequency', 'Distribution of HDD Storage Options')
    elif selected_column == 'SSD Storage':
        plot_countplot('SSD Storage', df, 'SSD Storage (GB)', 'Frequency', 'Distribution of SSD Storage Options')
    elif selected_column == 'Display Size':
        plot_countplot('Display Size', df, 'Display Size (inches)', 'Frequency', 'Distribution of Display Sizes')
    elif selected_column == 'Operating System':
        plot_countplot('Operating System', df, 'Operating System', 'Frequency', 'Distribution of Operating Systems')
    elif selected_column == 'Warranty':
        plot_countplot('Warranty', df, 'Warranty', 'Frequency', 'Distribution of Warranty Options')


st.header("Correlation Matrix")
# Create a correlation matrix
correlation_matrix = df.corr()
# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
st.pyplot(plt)


st.header(":red[More Insights With Respect To Brands]")
visualization_options = ['Average Price per Brand (Bar Chart)',
                         'Minimum Price per Brand (Bar Chart)',
                         'Maximum Price per Brand (Bar Chart)',
                         'Proportion of Products per Brand (Count Plot)',
                         'Scatter plot of Price vs. Rating (Colored by Brand)']

# Create a dropdown menu to select visualization
selected_option = st.selectbox('Select Visualization', visualization_options)

# Perform groupby based on selected visualization
if selected_option == 'Average Price per Brand (Bar Chart)':
    grouped_data = df.groupby('Brand')
    avg_prices = grouped_data['MRP'].mean()
    plt.figure(figsize=(10, 6))
    avg_prices.plot(kind='bar', rot=45)
    plt.xlabel('Brand')
    plt.ylabel('Average Price')
    plt.title('Average Price per Brand')
    plt.tight_layout()
    st.pyplot(plt)
elif selected_option == 'Minimum Price per Brand (Bar Chart)':
    grouped_data = df.groupby('Brand')
    min_prices = grouped_data['MRP'].min()
    plt.figure(figsize=(10, 6))
    min_prices.plot(kind='bar', rot=45)
    plt.xlabel('Brand')
    plt.ylabel('Minimum Price')
    plt.title('Minimum Price per Brand')
    plt.tight_layout()
    st.pyplot(plt) 
elif selected_option == 'Maximum Price per Brand (Bar Chart)':
    grouped_data = df.groupby('Brand')
    max_prices = grouped_data['MRP'].max()
    plt.figure(figsize=(10, 6))
    max_prices.plot(kind='bar', rot=45)
    plt.xlabel('Brand')
    plt.ylabel('Maximmum Price')
    plt.title('Maximum Price per Brand')
    plt.tight_layout()
    st.pyplot(plt)
elif selected_option == 'Proportion of Products per Brand (Count Plot)':
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Brand', data=df, palette='viridis')
    plt.xlabel('Brand')
    plt.ylabel('Product Count')
    plt.title('Proportion of Products per Brand')
    plt.tight_layout()
    plt.xticks(rotation=45)
    st.pyplot(plt)
elif selected_option == 'Scatter plot of Price vs. Rating (Colored by Brand)':
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='MRP', y='Rating', hue='Brand', data=df, palette='viridis',s=100)
    plt.xlabel('MRP')
    plt.ylabel('Rating')
    plt.title('Scatter plot of Price vs. Rating (Colored by Brand)')
    plt.tight_layout()
    st.pyplot(plt)





