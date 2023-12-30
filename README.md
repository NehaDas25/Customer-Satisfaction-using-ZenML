# Customer-Satisfaction-using-ZenML
Prediciting how a customer will feel about a product before they even ordered it using ZenML.

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zenml)](https://pypi.org/project/zenml/)

** Problem Statement **:
For a given customer's historical data, we are tasked to predict the review score for the next order or purchase. We will be using the [Brazilian ECommerce Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Objective
Achieve to predict the customer satisfaction score for a given order based on features like order status, price, payment, etc. 

To achieve this scenario in production, we will be using [ZenML](https://zenml.io/) to build a production ready pipeline to predict the customer satisfaction score for the next order or purchase.

This is to demonstrate how [ZenML](https://github.com/zenml-io/zenml) empowers the buisness to build and deploy ML pipelines in a multiple ways:
 - Providing a framework/template to baseline our purpose.
 - Integrate with [MLFlow](https://mlflow.org/) for deployment, tracking and many more.
 - Build and Deploy ML Pipelines smoothly.

## Snake: Python Requirements

Needed Python libraries for this project.

- Clone the project:
    ```bash
    $ git clone https://github.com/NehaDas25/Customer-Satisfaction-using-ZenML.git
    $ cd Customer-Satisfaction-using-ZenML
    $ pip install -r requirements.txt
    ```
    Install all the dependencies required.

- Install ZenML 0.20.0 for React based dashboard: This allows you to observe your stacks, stack components and pipeline statuses in dashboard of ZenML. [To Launch the ZenML Server and dashboard locally](https://docs.zenml.io/user-guide/starter-guide#explore-the-dashboard), but first install the dependencies.
    ``` bash
    $ pip install zenml["server"]
    $ zenml up
    ```


