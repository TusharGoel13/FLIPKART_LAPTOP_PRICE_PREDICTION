import streamlit as st
from matplotlib import image
import pandas as pd
import os
import re

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "laptop_details.csv")

st.set_page_config(page_title='Laptop Data Analysis')

st.header(":green[DataFrame]")
df = pd.read_csv(DATA_PATH)

########################################## Extract Features As Columns Using Regex #################################################

df['Brand'] = df['Product'].apply(lambda x : re.findall(r'^\w+', x))
df['Processor'] = df['Feature'].apply(lambda x : re.findall(r'(?:AMD|Intel|M1|M2)[\s+\w+]+Processor', x))
df['RAM Type'] = df['Feature'].apply(lambda x : re.findall(r'\d+\s+GB\s+(?:(?!and))(\w+|\w+\s+\w+)\s+RAM', x))
df['RAM Capacity (GB)'] = df['Feature'].apply(lambda x : re.findall(r'(\d+)\s+GB\s+(?:(?!and))\w+\s+RAM', x))

storage_capacity = df['Feature'].apply(lambda x: re.findall(r'(\d+)\s+(?:GB|TB)\s+(HDD|SSD)', x))
hdd_storage = []
ssd_storage = []

# Iterate through regex matches and store HDD and SSD storage capacities separately
for x in storage_capacity:
    hdd_found = False
    ssd_found = False
    for match in x:
        if match[1] == 'HDD' and not hdd_found:
            hdd_storage.append(float(match[0]))
            hdd_found = True
        elif match[1] == 'SSD' and not ssd_found:
            ssd_storage.append(float(match[0]))
            ssd_found = True
    if not hdd_found:
        hdd_storage.append(0.0)
    if not ssd_found:
        ssd_storage.append(0.0)
        
# Convert TB to GB if necessary
for i in range(len(hdd_storage)):
    if hdd_storage[i]==1.0:
        hdd_gb = hdd_storage[i] * 1024
        hdd_storage[i] = hdd_gb
        
for i in range(len(ssd_storage)):
    if ssd_storage[i]==1.0 or ssd_storage[i]==2.0:
        ssd_gb = ssd_storage[i] * 1024
        ssd_storage[i] = ssd_gb
        
# Assign the HDD and SSD storage capacities to the respective columns in the DataFrame
df['HDD Storage'] = hdd_storage
df['SSD Storage'] = ssd_storage

df['Operating System'] = df['Feature'].apply(lambda x : re.findall(r'(?:DOS|Mac\sOS|Chrome|\d+\sbit\s\w+\s\d+|Windows\s\d+)\sOperating System', x)[0])
df['Display Size'] = df['Feature'].apply(lambda x : list(set(re.findall(r'(\d\d\s?.?\d+)\s+(?:Inch|inch)', x))))
df['Warranty'] = df['Feature'].apply(lambda x : re.findall(r'(\d)\s+(?:Year|Years)(?:\s+\w+|\s+\w+\s+\w+)(?:�|\s)+Warranty', x) if re.findall(r'(\d)\s+(?:Year|Years)(?:\s+\w+|\s+\w+\s+\w+)(?:�|\s)+Warranty', x) else ['0'])


####################################################### Convert Feature Columns To String Or Float ###################################

df['Brand'] = df['Brand'].apply(lambda x : ''.join(x))
df['Processor'] = df['Processor'].apply(lambda x : ''.join(x))
df = df.loc[df['Processor'] != '', :]
df['RAM Type'] = df['RAM Type'].apply(lambda x : ''.join(x))
df['RAM Capacity (GB)'] = df['RAM Capacity (GB)'].apply(lambda x: float(x[0]) if x else 8.0)
df['Operating System'] = df['Operating System'].apply(lambda x : ''.join(x))
df['Display Size'] = df['Display Size'].apply(lambda x: float(x[0]) if x else 15.6)
df['Warranty'] = [float(val[0]) for val in df['Warranty']]
df['MRP'] = df['MRP'].apply(lambda x : x.replace('₹', '').replace(',', '')).astype(float)

df['Operating System'] = df['Operating System'].replace({'64 bit Windows 11 Operating System': 'Windows 11 Operating System',
                                                         '32 bit Windows 11 Operating System': 'Windows 11 Operating System',
                                                         '64 bit Windows 10 Operating System': 'Windows 10 Operating System'})

######################################################################################################################################
st.dataframe(df)

STORE_PATH = os.path.join(dir_of_interest, "data","laptop_details_modified.csv")
df.to_csv(STORE_PATH, index=False)

st.header(":red[Details of the Dataset]")
st.markdown("**Select on sidebar to view the details:**")
section = st.sidebar.radio('Select a section to view', ['Head', 'Tail', 'Columns', 'Shape', 'Descriptive Statistics', 'Data Types', 'Missing Values', 'Unique Values'])

# Display the first few rows of the dataset
if section == 'Head':
    st.subheader('First 5 rows')
    st.write(df.head())

# Display the last few rows of the dataset
elif section == 'Tail':
    st.subheader('Last 5 rows')
    st.write(df.tail())

# Display the columns of the dataset
elif section == 'Columns':
    st.subheader('Columns')
    st.write(df.columns)

# Display the shape of the dataset
elif section == 'Shape':
    st.subheader('Shape')
    st.write(df.shape)
    
# Display descriptive statistics for each variable
elif section == 'Descriptive Statistics':
    st.subheader('Descriptive Statistics')
    st.write(df.describe())

# Display data types
elif section == 'Data Types':
    st.subheader('Data Types')
    st.write(df.dtypes)

# Display missing values
elif section == 'Missing Values':
    st.subheader('Missing Values')
    st.write(df.isnull().sum())

# Display unique values
elif section == 'Unique Values':
    st.subheader('Unique Values')
    columns = ['Brand', 'Processor', 'RAM Type', 'RAM Capacity (GB)', 'HDD Storage', 'SSD Storage', 'Operating System', 'Display Size', 'Warranty']
    selected_column = st.selectbox('Select Column', columns)
    if selected_column:
        unique_values = df[selected_column].unique()
        unique_values.sort() 
        st.write(unique_values) 
    else:
        st.write('No column selected.') 

