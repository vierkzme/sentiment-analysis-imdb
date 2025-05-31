# 🎬 IMDB Movie Review Sentiment Analysis 🎭

A simple **Machine Learning** project using Python to analyze sentiment in IMDB movie reviews. This project covers text preprocessing, model training, performance evaluation, and an interactive web app using **Streamlit**.

---

## 📌 Project Features

✅ Text preprocessing (cleaning, stopword removal, stemming)  
✅ Text transformation using **TF-IDF Vectorizer**  
✅ Sentiment classification using **Logistic Regression**  
✅ Model evaluation with **confusion matrix**  
✅ Web demo app for real-time sentiment prediction

---

## 🗂️ Project Structure

```
sentiment-app/
│
├── app.py                  # Streamlit application
├── model.pkl               # Trained classification model
├── vectorizer.pkl          # Trained TF-IDF vectorizer
├── IMDB Dataset.csv        # Movie review dataset (100k samples)
├── train_model.py          # Script to train model and save .pkl files
├── test_load.py            # Script to verify model/vectorizer compatibility
├── requirements.txt        # Project dependencies
└── README.md               # This documentation
```

---

## 🧠 Algorithms Used

- **Text Preprocessing**: BeautifulSoup, RegEx, Stopword Removal, Stemming
- **TF-IDF Vectorization**: Converts text into numerical features
- **Logistic Regression**: Main classification algorithm
- **Scikit-learn**: For training, evaluation, and model serialization

---

## 🧪 Review Examples

```text
"The movie was an absolute masterpiece. The performances were stunning."
→ Model prediction: POSITIVE 😊

"This was the worst movie I’ve ever seen. I walked out of the theater."
→ Model prediction: NEGATIVE 😞
```

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/vierkzme/sentiment-analysis-imdb
cd sentiment-analysis-imdb
```

### 2. Install dependencies (use virtual environment recommended)

```bash
pip install -r requirements.txt
```

### 3. Launch the application

```bash
streamlit run app.py
```

---

📊 Hasil Evaluasi
Confusion Matrix dari hasil uji pada data test (20%):

Predicted Positif Predicted Negatif
Actual Positif TP = xx FN = xx
Actual Negatif FP = xx TN = xx

(⚠️ Angka di atas bisa diisi sesuai hasil evaluasi kamu.)

---

⚠️ Catatan Penting
Pastikan versi scikit-learn saat melatih dan memuat model harus sama (disarankan 1.6.1) agar file .pkl bisa digunakan tanpa error.
Gunakan test_load.py untuk memastikan file model dan vectorizer bisa digunakan sebelum dipakai di app.py.

📎 Lisensi
Proyek ini dirilis dengan MIT License — silakan digunakan, dimodifikasi, dan dibagikan dengan bebas.

Dibuat dengan ❤️ oleh Ardy Nugroho sebagai bagian dari portfolio data science pribadi.
