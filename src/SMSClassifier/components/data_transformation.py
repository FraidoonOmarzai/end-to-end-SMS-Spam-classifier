from src.SMSClassifier.logging import logger
from src.SMSClassifier.entity.config_entity import DataTransformationConfig
import pandas as pd

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

import os


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def prepare_data(self):
        df = pd.read_csv(self.config.data_path, encoding='latin-1')
        # print(df.head(2))

        # remove unnecessary columns
        df = df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1)

        # rename columns name
        df = df.rename(columns={'v1': 'target', 'v2': 'msg'})

        # remove duplicates
        df = df.drop_duplicates(keep='first')

        # label encoding
        df.target = df.target.replace({'ham': 0, 'spam': 1})

        # text preprocessing
        df.msg = df.msg.apply(self.clean_msg)

        # save the dataset
        df.to_csv(os.path.join(self.config.root_dir,
                  'clean_df.csv.'), index=False)

    def clean_msg(self, msg, stemmer=PorterStemmer(), stop_words=set(stopwords.words('english'))):

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
