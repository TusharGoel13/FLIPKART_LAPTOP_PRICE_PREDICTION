import streamlit as st

# Set page configuration
st.set_page_config(
    page_title='FLIPKART LAPTOP PRICE PREDICTOR',
    page_icon=':computer:',
    layout='wide',
    initial_sidebar_state='auto'
)

# Main title
st.title(":red[Hello Everyone] :wave: ")

# Header
st.header("I am :green[Tushar Goel] and I welcome you to my :blue[Laptop Price Webapp!]")
st.subheader("This interactive webapp, powered by streamlit, provides you with a seamless experience to analyze and visualize the :orange[Flipkart Laptop Dataset], along with the ability to predict laptop prices based on user inputs.")
st.subheader("With this webapp, you can effortlessly create various plots and charts to explore and analyze the dataset, with the added flexibility of choosing your desired X-axis and Y-axis for visualization. This empowers you to gain insights and make informed decisions based on the data at hand.")
st.subheader("Whether you are interested in data analysis or visualization, or looking to predict laptop prices based on specific parameters, this webapp offers a user-friendly interface to meet your requirements. Get ready to uncover meaningful patterns and trends in the dataset, and leverage the power of data to make informed decisions.")
st.subheader(":green[Feel free to connect with me :]")

# Add LinkedIn and GitHub links
link = '[![Title](https://camo.githubusercontent.com/5e3d78e5310a41c0667e07077cf93596229de398b154b83885dc068874ed5365/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d2532333145373742352e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/in/tushar-goel04/)'
st.markdown(link,unsafe_allow_html=True)
link2 = '[![Title](https://camo.githubusercontent.com/b2d1ae072c968dbeaf2232f0e1071ae5a7b218b11caec1ae5c69c10ef370a3cc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d2532333234323932652e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465)](https://github.com/TusharGoel13)'
st.markdown(link2,unsafe_allow_html=True)
