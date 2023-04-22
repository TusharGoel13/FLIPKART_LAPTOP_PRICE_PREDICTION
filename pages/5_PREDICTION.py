import streamlit as st
import pandas as pd
import os
import re
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title='Laptop MRP Prediciton')
st.title(":blue[MRP Prediction]")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "laptop_details_modified.csv")

df = pd.read_csv(DATA_PATH)

# Define the columns to encode
columns_to_encode = ['Brand', 'Processor', 'RAM Type', 'Operating System']

# Perform label encoding on the dataframe
df_encoded = df.copy()
label_encodings = {}
for col in columns_to_encode:
    encoder = LabelEncoder()
    df_encoded[col] = encoder.fit_transform(df[col])
    label_encodings[col] = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))

# Create the Streamlit web application
st.write('Enter the details below to predict MRP for a product')

# Get the selected brand, processor, ram type, and operating system values
brand_name = st.selectbox('Brand', list(label_encodings['Brand'].keys()))
processor_name = st.selectbox('Processor', list(label_encodings['Processor'].keys()))
ram_type_name = st.selectbox('RAM Type', list(label_encodings['RAM Type'].keys()))
operating_system_name = st.selectbox('Operating System',list(label_encodings['Operating System'].keys()))

# Get the corresponding encoded values from the label encodings
brand = label_encodings['Brand'][brand_name]
processor = label_encodings['Processor'][processor_name]
ram_type = label_encodings['RAM Type'][ram_type_name]
operating_system = label_encodings['Operating System'][operating_system_name]

# Continue with the rest of the code
ram_capacity = st.slider('RAM Capacity (GB)', min_value=4, max_value=64, value=8,step=4)
hdd_storage = st.number_input('HDD Storage (GB)', min_value=0, max_value=2048,value=0,step=128)
ssd_storage = st.number_input('SSD Storage (GB)', min_value=0, max_value=2048,value=256,step=128)
display_size = st.number_input('Display Size (inches)', value=15.6)
warranty = st.number_input('Warranty (years)', value=1)

# Create a dataframe from user input
if hdd_storage == 0 and ssd_storage == 0:
    st.warning("Both HDD storage and SSD storage cannot be 0 at the same time.")
else :
    new_data = pd.DataFrame({'Brand': [brand], 'Processor': [processor],
                            'RAM Type': [ram_type], 'RAM Capacity (GB)': [ram_capacity],
                            'HDD Storage': [hdd_storage], 'SSD Storage': [ssd_storage],
                            'Operating System': [operating_system], 'Display Size': [display_size],
                            'Warranty': [warranty]})
    
   
    
    
# Perform prediction on user input
reg_model = LinearRegression()
X = df_encoded.drop(['Product', 'Rating', 'MRP', 'Feature'], axis=1)
y = df_encoded['MRP']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
reg_model.fit(X_train, y_train)
y_pred = reg_model.predict(X_test)

# Display the prediction result
# Add a button widget
prediction_button = st.button('Predict MRP')

# Check if the button is clicked
if prediction_button:
    # Perform prediction and get the result
    new_prediction = reg_model.predict(new_data)
    # Display the prediction result
    st.write('MRP Prediction:', new_prediction[0])
    
    st.markdown('**User-selected entries:**')
    st.markdown(f'**Brand:** {brand_name}')
    st.markdown(f'**Processor:** {processor_name}')
    st.markdown(f'**Operating System:** {operating_system_name}')
    st.markdown(f'**RAM Type:** {ram_type_name}')
    st.markdown(f'**RAM Capacity (GB):** {ram_capacity}')
    st.markdown(f'**HDD Storage (GB):** {hdd_storage}')
    st.markdown(f'**SSD Storage (GB):** {ssd_storage}')
    st.markdown(f'**Display Size (inches):** {display_size}')
    st.markdown(f'**Warranty (years):** {warranty}')
