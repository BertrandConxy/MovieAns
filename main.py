from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


# from queries.query_results import run_query
# from queries.analysis_queries import total_sales_by_product

def run_etl_pipeline():
    # Step 1: Extract
    file_path = 'data/movies.csv'
    data = extract_data(file_path)

    # Step 2: Transform
    cleaned_data = transform_data(data)

    # Step 3: Load
    db_path = 'db/movies.db'
    load_data(cleaned_data, db_path)

    # # Step 4: Analyze
    # query = total_sales_by_product()
    # result = run_query(db_path, query)
    # print(result)


if __name__ == "__main__":
    run_etl_pipeline()
