import pandas as pd
import os


def extract_data(file_path):
    """
    Extracts data from a CSV file and loads it into a pandas DataFrame.

    Args:
    - file_path (str): The path to the CSV file.

    Returns:
    - DataFrame: A pandas DataFrame containing the extracted data.

    Raises:
    - FileNotFoundError: If the file is not found at the given path.
    - ValueError: If the file format is incorrect or cannot be read.
    - Exception: For any other generic errors.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        print(f"Successfully extracted data from {file_path}")
        return df
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file at {file_path} is empty or invalid.")
    except pd.errors.ParserError:
        raise ValueError(f"Failed to parse the CSV file at {file_path}. It may be malformed.")
    except Exception as e:
        # Catch all other exceptions and re-raise them for visibility
        raise Exception(f"An error occurred while reading the file: {e}")
