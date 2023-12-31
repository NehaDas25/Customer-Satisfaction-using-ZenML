from pipelines.training_pipeline import train_pipeline
#from zenml.integrations.mlflow.mlflow_utils import get_tracking_uri
from zenml.client import Client

if __name__ == "__main__":
    stack_instance = Client().active_stack
    print(f"Type of stack_instance: {type(stack_instance)}")
    tracking_url = stack_instance.experiment_tracker.get_tracking_uri()
    print(tracking_url)
    training = train_pipeline("data\olist_customers_dataset.csv")
    #training.run()