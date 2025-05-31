import pickle

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

print("IDF size:", len(vectorizer.idf_))  # Harus berhasil
