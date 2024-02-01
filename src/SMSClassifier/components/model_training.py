from src.SMSClassifier.logging import logger
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from src.SMSClassifier.entity.config_entity import ModelTrainingConfig
import joblib
import pandas as pd
import os


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig) -> None:
        self.config = config

    def training_pipeline(self):
        df = pd.read_csv(self.config.df, encoding='latin-1')
        # print(df.head(2))

        # tfidf vectorizer
        tfv = TfidfVectorizer(max_features=2500)
        X = tfv.fit_transform(df['msg'].values.astype('U'))

        y = df.target

        # balance the dataset
        sampler = RandomOverSampler(random_state=42)
        X_sm, y_sm = sampler.fit_resample(X, y)

        # train test split
        X_train, X_test, y_train, y_test = train_test_split(
            X_sm, y_sm, test_size=0.20, random_state=42)

        # train the model
        model = MultinomialNB()
        model.fit(X_train, y_train)

        # model evaluation
        y_pred = model.predict(X_test)
        logger.info(confusion_matrix(y_test, y_pred))

        logger.info(classification_report(y_test, y_pred))

        # save the model
        # save_bin(model, os.path.join(self.config.root_dir, 'model.joblib'))
        joblib.dump(model, os.path.join(self.config.root_dir, 'model.joblib'))
        joblib.dump(tfv, os.path.join(self.config.root_dir, 'tfidfv.joblib'))
