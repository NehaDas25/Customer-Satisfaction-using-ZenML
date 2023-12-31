from pipelines.training_pipeline import train_pipeline
from steps.clean_data import clean_df
from steps.evaluate import evaluate_model
from steps.ingest_data import ingest_df
from steps.model_train import train_model
#from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri

if __name__ == "__main__":
    training = train_pipeline("data\olist_customers_dataset.csv")
    #training.run()