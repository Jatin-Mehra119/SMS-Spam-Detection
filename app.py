import streamlit as st
import joblib
from PIL import Image

# Load the model
model = joblib.load('spam_model.pkl')

# Set the page configuration
st.set_page_config(page_title="Spam Detection App", page_icon="📧", layout="wide")

# Custom CSS for background and styling
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.transparenttextures.com/patterns/fancy-deboss.png");
    }
    .sidebar .sidebar-content {
        background: url("https://www.transparenttextures.com/patterns/fancy-deboss.png");
    }
    .logo-container {
        display: flex;
        align-items: center;
    }
    .logo {
        width: 80px;
        margin-right: 20px;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a logo and title
st.markdown(
    """
    <div class="logo-container">
        <img src="https://student.elon.edu/jparham/public_html/spamproj/spamWordCloud.png" class="logo" alt="Spam Detection Logo">
        <h1>Spam Detection App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Description and separator
st.write("This app detects spam in messages using a machine learning model.")
st.markdown('---')

# Input area with some styling
st.header("Enter a message to check if it is spam or not:")
message = st.text_area("Type your message here:", height=150)

# Add a button and display the result
if st.button("Check", key='check_button'):
    if message == '':
        st.warning("Please enter a message to check.")
    else:
        pred = model.predict([message])
        st.markdown('---')
        if pred[0] == 'spam':
            st.error(f"The message is: **{pred[0].upper()}**")
        else:
            st.success(f"The message is: **{pred[0].upper()}**")

# Add footer
st.markdown(
    """
    <div class="footer">
        <p>Developed by Jatin Mehra.</p>
    </div>
    """,
    unsafe_allow_html=True
)