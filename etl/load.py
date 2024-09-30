import sqlite3


def load_data(df, db_path):
    """
    Loads a pandas DataFrame into an SQLite database.

    Args:
    - df (DataFrame): The pandas DataFrame to load.
    - db_path (str): The path to the SQLite database file.

    Raises:
    - ValueError: If the DataFrame is empty.
    - sqlite3.DatabaseError: For database connection or execution errors.
    """
    # Ensure the DataFrame is not empty
    if df.empty:
        raise ValueError("The DataFrame is empty and cannot be loaded into the database.")

    try:
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(db_path)

        # Load the DataFrame into the database
        df.to_sql('movies_data', conn, if_exists='replace', index=False)
        conn.commit()

        print("Data successfully loaded into the database.")
        conn.close()
    except sqlite3.DatabaseError as db_error:
        raise sqlite3.DatabaseError(f"An error occurred while loading data to the database: {db_error}")

    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
