import sys
import os
from textblob import TextBlob
import csv
import nltk
nltk.download('punkt')


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


with open(resource_path("test_text.csv"), 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        try:
            sentence = row[0]
            blob = TextBlob(sentence)
            print(blob.word_counts)
            print(sentence)
            print(blob.sentiment.polarity, blob.sentiment.subjectivity)
        except:
            print("This line is blank.")
