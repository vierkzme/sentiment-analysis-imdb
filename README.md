# 🎬 Sentiment Analysis Ulasan Film IMDB 🎭

Sebuah proyek **Machine Learning** sederhana menggunakan Python untuk menganalisis sentimen dari ulasan film IMDB. Proyek ini mencakup proses preprocessing teks, pelatihan model, evaluasi performa, serta sebuah aplikasi web interaktif menggunakan **Streamlit**.

---

## 📌 Fitur Proyek

✅ Preprocessing teks ulasan (cleaning, stopword removal, stemming)  
✅ Transformasi data teks menggunakan **TF-IDF Vectorizer**  
✅ Pelatihan model klasifikasi menggunakan **Logistic Regression**  
✅ Evaluasi performa model menggunakan **confusion matrix**  
✅ Aplikasi demo berbasis web untuk prediksi sentimen ulasan secara real-time

---

## 🗂️ Struktur Folder

sentiment-app/
├── app.py # Aplikasi Streamlit
├── model.pkl # Model klasifikasi yang sudah dilatih
├── vectorizer.pkl # TF-IDF Vectorizer yang sudah dilatih
├── test_load.py # Script pengecekan kompatibilitas versi model/vectorizer
├── requirements.txt # Daftar dependensi proyek
└── README.md # Dokumentasi proyek ini


---

## 🧠 Algoritma yang Digunakan

- **Text Preprocessing**: BeautifulSoup, RegEx, Stopword Removal, Stemming
- **TF-IDF Vectorization**: Untuk mengubah teks menjadi fitur numerik
- **Logistic Regression**: Sebagai algoritma klasifikasi utama
- **Scikit-learn**: Untuk training, evaluasi, dan serialization model

---

## 🧪 Contoh Ulasan

"The movie was an absolute masterpiece. The performances were stunning."
→ Model memprediksi: POSITIF 😊

"This was the worst movie I’ve ever seen. I walked out of the theater."
→ Model memprediksi: NEGATIF 😞

---

🚀 Jalankan Proyek Ini Secara Lokal
1. Clone repository
git clone https://github.com/vierkzme/sentiment-analysis-imdb
cd sentiment-analysis-imdb

2. Install dependency (disarankan gunakan virtual environment)
pip install -r requirements.txt

3. Jalankan aplikasi
streamlit run app.py

---

📊 Hasil Evaluasi
Confusion Matrix dari hasil uji pada data test (20%):

Predicted Positif	Predicted Negatif
Actual Positif	TP = xx	FN = xx
Actual Negatif	FP = xx	TN = xx

(⚠️ Angka di atas bisa diisi sesuai hasil evaluasi kamu.)

---

⚠️ Catatan Penting
Pastikan versi scikit-learn saat melatih dan memuat model harus sama (disarankan 1.6.1) agar file .pkl bisa digunakan tanpa error.
Gunakan test_load.py untuk memastikan file model dan vectorizer bisa digunakan sebelum dipakai di app.py.

📄 License
MIT License © 2025 – vierkzme
silakan digunakan, dimodifikasi, dan dibagikan dengan bebas.
