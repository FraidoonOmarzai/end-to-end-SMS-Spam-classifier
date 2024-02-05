from src.SMSClassifier.logging import logger
from src.SMSClassifier.entity.config_entity import DataTransformationConfig
import pandas as pd

import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from collections import Counter


import os


class DataTransformation1:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def clean_data(self):
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

        return df

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

    def tfidf_vectorizer(self, df):
        # tfidfvectorizer

        tfv = TfidfVectorizer(max_features=2500)
        X = tfv.fit_transform(df['msg']).toarray()
        y = df['target']

        df_new = pd.DataFrame(X, index=df.index)
        df_new['target'] = y

        logger.info(f'after tfidf data shape: {df_new.shape}')

        return df_new

    def handle_imbalance(self, df):
        # balance the dataset
        X = df.drop('target', axis=1)
        y = df.target

        sampler = RandomOverSampler(random_state=42)
        X_sm, y_sm = sampler.fit_resample(X, y)

        logger.info('Resampled dataset shape %s' % Counter(y_sm))

        df_new = pd.DataFrame(X_sm, index=df.index)
        df_new['target'] = y_sm

        logger.info(df_new.shape)

        return df_new

    def train_test_splits(self, df):
        train, test = train_test_split(df)
        train.to_csv(os.path.join(
            self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, "test.csv"), index=False)
        logger.info("Splited data into training and test sets")
        logger.info(f'train shape: {train.shape}')
        logger.info(f'test shape: {test.shape}')
