import streamlit as st
import pickle
import re

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load TF-IDF vectorizer
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Text cleaning function
def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Remove extra spaces
    text = text.split()
    text = ' '.join(text)

    return text


# Streamlit page settings
st.set_page_config(
    page_title="Fake News Detection App",
    page_icon="📰",
    layout="centered"
)

# Title
st.title("📰 Fake News Detection App")

# Description
st.write(
    "Enter a news article or headline below to check whether it is Fake or Real."
)

# Text input box
input_news = st.text_area(
    "Enter News Text Here",
    height=200
)

# Predict button
if st.button("Predict"):

    # Check if input is empty
    if input_news.strip() == "":
        st.warning("Please enter some news text.")
    
    else:
        # Clean text
        cleaned_text = clean_text(input_news)

        # Convert text to vector
        vector_input = vectorizer.transform([cleaned_text])

        # Predict
        prediction = model.predict(vector_input)

        # Show result
        if prediction[0] == 0:
            st.error("🚨 This News is FAKE")
        else:
            st.success("✅ This News is REAL")
