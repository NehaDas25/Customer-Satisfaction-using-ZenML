import logging
import pandas as pd
from zenml import step
from src.data_cleaning import DataCleaning, DataDivideStrategy, DataPreProcessingStrategy
from typing_extensions import Annotated
from typing import Tuple

@step
def clean_df(df: pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, "X_train"],
    Annotated[pd.DataFrame, "X_test"],
    Annotated[pd.Series, "y_train"],
    Annotated[pd.Series, "y_test"],
]:
    try:
        process_strategy = DataPreProcessingStrategy()
        data_cleaning = DataCleaning(df, process_strategy)
        processed_data = data_cleaning.handle_data()

        divide_strategy = DataDivideStrategy()
        data_divide_strategy = DataCleaning(processed_data, divide_strategy)
        X_train, X_test, y_train, y_test = data_divide_strategy.handle_data()
        logging.info("Data Cleaning completed")
        return X_train, X_test, y_train, y_test
    except Exception as E:
        logging.error("Error in dividing data: {}".format(E))
        raise E