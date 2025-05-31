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
st.title("Analisis Sentimen Film IMDB")
review = st.text_area("Masukkan ulasan film di sini:")

if st.button("Prediksi Sentimen"):
    if review:
        clean_text = preprocess(review)
        vectorized = vectorizer.transform([clean_text])
        prediction = model.predict(vectorized)

        result = "Positif 😊" if prediction[0] == 1 else "Negatif 😞"
        st.subheader(f"Hasil Prediksi: {result}")
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")
