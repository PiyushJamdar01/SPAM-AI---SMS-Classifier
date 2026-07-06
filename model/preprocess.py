import re
import nltk
from nltk.corpus import stopwords

# Download stopwords only if they are not already available
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("english"))


def clean_text(text):
    """
    Cleans an SMS message before prediction.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters (keep letters, $ and £)
    text = re.sub(r'[^a-zA-Z$£\s]', '', text)

    # Remove extra spaces
    text = text.strip()

    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]

    # Join the words back into a sentence
    return " ".join(words)