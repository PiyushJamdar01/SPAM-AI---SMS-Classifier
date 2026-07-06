from flask import Flask, request, render_template, jsonify
import pickle

from model.preprocess import clean_text
from database import save_prediction, get_all_predictions

# Create Flask application
app = Flask(__name__)

# Load trained spam model
with open("model/spam_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load TF-IDF Vectorizer
with open("model/tfidf_vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


# ============================================
# ROUTE 1 — HOME PAGE
# ============================================
@app.route("/")
def home():
    return render_template("index.html")


# ============================================
# ROUTE 2 — PREDICT
# ============================================
@app.route("/predict", methods=["POST"])
def predict():

    print("\n========== NEW REQUEST ==========")

    print("1. Request received")

    data = request.get_json()

    print("2. JSON received:", data)

    message = data["message"]

    print("3. Message:", message)

    # Clean the user's message
    cleaned_message = clean_text(message)

    print("4. Cleaned Message:", cleaned_message)

    # Convert cleaned text into TF-IDF features
    message_vector = vectorizer.transform([cleaned_message])

    print("5. Vectorization Complete")

    # Predict using the trained model
    prediction = model.predict(message_vector)[0]

    print("6. Prediction:", prediction)

    # Convert prediction into a readable label
    if prediction == 1:
        label = "SPAM"
    else:
        label = "SAFE"

    print("7. Label:", label)

    # Get prediction probabilities
    probabilities = model.predict_proba(message_vector)[0]

    print("8. Probabilities:", probabilities)

    # Calculate confidence percentage
    confidence = round(max(probabilities) * 100, 2)

    print("9. Confidence:", confidence)

    # Save prediction to MongoDB
    print("10. Saving prediction to MongoDB...")

    save_prediction(
        message,
        cleaned_message,
        label,
        confidence
    )

    print("11. Saved Successfully!")

    # Return prediction to frontend
    return jsonify({
        "label": label,
        "confidence": confidence,
        "message": message
    })


# ============================================
# ROUTE 3 — HISTORY
# ============================================
@app.route("/history")
def history():
    records = get_all_predictions()
    print("History Records:", records)   # <-- Add this line
    return render_template("history.html", records=records)


# ============================================
# RUN APP
# ============================================
if __name__ == "__main__":
    app.run(debug=True)