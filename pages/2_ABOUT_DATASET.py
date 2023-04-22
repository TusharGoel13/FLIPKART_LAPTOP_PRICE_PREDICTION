import streamlit as st
from matplotlib import image
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "laptop.jpg")

st.set_page_config(page_title='About Flipkart Laptop Dataset')
st.title(":blue[Flipkart Laptop Dataset]")

img = image.imread(IMAGE_PATH)
st.image(img)


st.header(":red[Dataset]")
st.markdown("**The Flipkart Laptop Dataset provides detailed information on 720 laptops available on Flipkart, one of India's largest e-commerce websites. The dataset includes technical specifications, ratings, and prices.**")
st.markdown("**Aside: In the fast-paced digital era, laptops have become indispensable tools for work, education, and entertainment.**")

st.header(":orange[Attributes]")
st.markdown("**:computer: :violet[_BRAND:_] The brand name of the laptop**")
st.markdown("**:computer: :violet[_PRICE:_] The price of the laptop in Indian Rupees**")
st.markdown("**:computer: :violet[_RATING:_] The average rating of the laptop**")
st.markdown("**:computer: :violet[_SPECIFICATIONS:_] Technical specifications of the laptop, including processor, RAM, storage, display, graphics, etc.**")

st.header(":green[Use Cases]")
st.markdown("**:dart: :violet[_MARKET RESEARCH:_]  Analysts and researchers can use this dataset to analyze the Indian laptop market, identify trends, and make data-driven business decisions.**")
st.markdown("**:dart: :violet[_PRODUCT COMPARISON:_]  Consumers can compare various laptop models based on specifications, ratings, and prices to make informed purchase decisions.**")
st.markdown("**:dart: :violet[_GAMING:_]  Gamers can use this dataset to find laptops with high-performance specifications for gaming purposes.**")
st.markdown("**:dart: :violet[_PERSONAL USE:_]  Individuals can explore the dataset to find laptops that meet their specific needs, such as for work, education, or entertainment.**")
