import sqlite3
import pandas as pd
from queries.analysis_queries import rank_movies_by_popularity


def run_query(db_path, query):
    conn = sqlite3.connect(db_path)
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result


if __name__ == "__main__":
    db_path = '../db/movies.db'
    query = rank_movies_by_popularity()
    result = run_query(db_path, query)
    print(result)
