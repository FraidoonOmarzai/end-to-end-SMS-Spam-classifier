from src.SMSClassifier.logging import logger
from sklearn.naive_bayes import MultinomialNB
from sklarn.model_selection import RandomizedSearchCV
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

        grid = {
            "alpha": [0.00001, 0.0001, 0.001, 0.1, 1, 10, 100, 1000],
            "force_alpha": [True, False]
        }

        model_rs = RandomizedSearchCV(estimator=MultinomialNB(),
                                      param_distributions=grid,
                                      n_iter=5,
                                      verbose=False)
        model_rs.fit(X_train, y_train)

        best_params = model_rs.best_params_

        logger.info(best_params)

        # train the model
        model = MultinomialNB(**best_params)
        model.fit(X_train, y_train)

        logger.info(f"Model train score: {model.score(X_train, y_train)}")

        # save the model
        joblib.dump(model, os.path.join(self.config.root_dir, 'model.joblib'))
