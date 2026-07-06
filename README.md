# 📩 Spam SMS Classifier

A Machine Learning web application that classifies SMS messages as **Spam** or **Ham (Safe)** using **Multinomial Naive Bayes** and **TF-IDF Vectorization**. The application is built with **Flask** and stores prediction history in **MongoDB Atlas**.

---

## 🚀 Features

- Detects whether an SMS is Spam or Ham
- Text preprocessing using NLTK
- TF-IDF Vectorization
- Multinomial Naive Bayes Classifier
- Displays prediction confidence
- Stores prediction history in MongoDB Atlas
- View prediction history through a web interface
- Responsive user interface built with HTML, CSS and JavaScript

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- NLTK
- MongoDB Atlas
- HTML
- CSS
- JavaScript
- Google Colab
- VS Code

---

## 📂 Project Structure

```text
spam-classifier/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
│
├── data/
│   └── spam.csv
│
├── model/
│   ├── preprocess.py
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── index.html
│   └── history.html
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd spam-classifier
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

Set your MongoDB connection string before running the app:

```bash
set MONGODB_URI=your_mongodb_connection_string
```

On PowerShell:

```powershell
$env:MONGODB_URI = "your_mongodb_connection_string"
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Pipeline

1. User enters an SMS message.
2. Flask receives the request.
3. The message is cleaned using NLTK preprocessing.
4. TF-IDF converts the cleaned text into numerical features.
5. The trained Multinomial Naive Bayes model predicts Spam or Ham.
6. The prediction and confidence score are displayed.
7. The prediction is stored in MongoDB Atlas.

---

## 🗄️ Database

MongoDB Atlas stores:

- Original message
- Cleaned message
- Prediction
- Confidence score
- Timestamp

---

## 👨‍💻 Author

**Piyush Jamdar**