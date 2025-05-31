import streamlit as st
import pickle
import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('stopwords')

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Preprocessing function
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


def preprocess(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub("[^a-zA-Z]", " ", text)
    words = text.lower().split()
    words = [stemmer.stem(w) for w in words if w not in stop_words]
    return " ".join(words)


# Streamlit UI
st.title("IMDB Movie Sentiment Analysis")
review = st.text_area("Enter movie reviews here:")

if st.button("Sentiment Prediction"):
    if review:
        clean_text = preprocess(review)
        vectorized = vectorizer.transform([clean_text])
        prediction = model.predict(vectorized)

        result = "Positive 😊" if prediction[0] == 1 else "Negative 😞"
        st.subheader(f"Predicted Results: {result}")
    else:
        st.warning("Please enter the text first.")
