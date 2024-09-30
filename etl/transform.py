import pandas as pd
import os


def transform_data(df):
    """
    Transform the passed in dataframe and returns the transformed dataframe.

    Args:
    - df

    Returns:
    - df

    Raises:
    - FileNotFoundError: If the file is not found at the given path.
    - ValueError: If the file format is incorrect or cannot be read.
    - Exception: For any other generic errors.
    """

    try:
        cleaned_df = df.dropna()
        cut_df = cleaned_df[0:1000]
        return cut_df
    except KeyError as e:
        raise KeyError(f"Column error: {e}")
    except ValueError:
        raise ValueError(f"Failed to convert 'Order_Date' to datetime. Please check the format.")
    except TypeError as e:
        raise TypeError(f"Type error: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
