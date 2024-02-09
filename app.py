import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from pathlib import Path

import streamlit as st
import joblib
import string


def clean_msg(msg, stemmer=PorterStemmer(), stop_words=set(stopwords.words('english'))):

    # remove html tags
    soup = BeautifulSoup(msg, 'html.parser')
    clean_text = soup.get_text()

    # convert to lower case and splits up the words
    words = word_tokenize(clean_text.lower())

    filter_words = []

    for word in words:
        # removing the stop words and punctuation
        if word not in stop_words and word.isalpha():
            filter_words.append(stemmer.stem(word))  # words stemming

    return ' '.join(filter_words)


# loading tfidf and saved model
tfidf = joblib.load(Path('artifacts/data_transformation/tfidfv.joblib'))
model = joblib.load(Path('artifacts/model_training/model.joblib'))


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # 1. preprocess msg
    transformed_sms = clean_msg(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
