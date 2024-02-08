from src.SMSClassifier.logging import logger
from src.SMSClassifier.entity.config_entity import ModelEvaluationConfig
from src.SMSClassifier.utils.common import save_json
from pathlib import Path
import pandas as pd
import joblib

from sklearn.metrics import f1_score, precision_score, recall_score

import mlflow
from urllib.parse import urlparse


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config

    def eval_metrics(self, y_true, y_pred):
        f1 = f1_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)

        return f1, precision, recall

    def model_evaluation(self):
        test_df = pd.read_csv(self.config.test_path)
        model = joblib.load(self.config.model_path)

        X_test, y_test = test_df.drop('target', axis=1), test_df['target']

        mlflow.set_experiment(self.config.experiment_name)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        with mlflow.start_run(run_name=self.config.run_name):

            y_pred = model.predict(X_test)

            (f1, precision, recall) = self.eval_metrics(y_test, y_pred)

            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)
            mlflow.log_metric("f1", f1)

            # Saving metrics as local
            scores = {"f1": f1, "precision": precision, "recall": recall}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="MultinomialNB")
            else:
                mlflow.sklearn.log_model(model, "model")
