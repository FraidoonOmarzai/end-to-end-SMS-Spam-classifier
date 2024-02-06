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
        train_path = pd.read_csv(self.config.train_path)

        X_train = train_path.drop('target', axis=1)
        y_train = train_path['target']

        # train the model
        model = MultinomialNB()
        model.fit(X_train, y_train)

        logger.info(f"Model train score: {model.score(X_train, y_train)}")

        # save the model
        joblib.dump(model, os.path.join(self.config.root_dir, 'model.joblib'))
