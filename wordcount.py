# Required Modules for python
import requests
from bs4 import BeautifulSoup
import json
import nltk
from nltk.corpus import stopwords


# Word Frequency Function
def get_word_frequency(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text = soup.get_text()

    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]

    frequency = nltk.FreqDist(filtered_tokens)

    word_frequency_list = [(word, freq) for word, freq in frequency.items()]

    word_frequency_json = json.dumps(word_frequency_list)

    return word_frequency_json


# Driver Mechanism
url = "https://practice.geeksforgeeks.org/"
word_frequency_json = get_word_frequency(url)
print(word_frequency_json)
