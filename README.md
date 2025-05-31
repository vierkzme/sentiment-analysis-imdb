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

* **Text Preprocessing**: BeautifulSoup, RegEx, Stopword Removal, Stemming
* **TF-IDF Vectorization**: Converts text into numerical features
* **Logistic Regression**: Main classification algorithm
* **Scikit-learn**: For training, evaluation, and model serialization

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
git clone https://github.com/username/sentiment-analysis-imdb.git
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

## ⚙️ Retrain the Model (Optional)

If you want to retrain the model:

```bash
python train_model.py
```

This will regenerate `model.pkl` and `vectorizer.pkl`.

---

## 📊 Evaluation Results

Confusion Matrix from test data (20%):

|                     | Predicted Positive | Predicted Negative |
| ------------------- | ------------------ | ------------------ |
| **Actual Positive** | TP = xx            | FN = xx            |
| **Actual Negative** | FP = xx            | TN = xx            |

(⚠️ Replace values above with your actual results.)

---

## 📦 Requirements

```
pandas
numpy
scikit-learn==1.6.1
nltk
beautifulsoup4
streamlit
```

---

## ⚠️ Important Notes

* Make sure the version of `scikit-learn` used to **train** and **load** the model is the **same** (recommended: `1.6.1`) to avoid `.pkl` file errors.
* Use `test_load.py` to verify the model and vectorizer before using in `app.py`.

---

## 📄 License

MIT License © 2025 – vierkzme
Please feel free to use, modify and share freely.
