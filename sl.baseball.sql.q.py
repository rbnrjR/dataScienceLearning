import pandas as pd


def query_data(path_to_csv, path_to_new_csv):
    baseball_data = pd.read_csv(path_to_csv)
    q = '''
    SELECT
    nameFirst, nameLast
    FROM
    baseball_data
    LIMIT
    20
    '''

    try:
    	baseball_solution = execute_sql(q)
    except Exception as e:
    	print('error in executing sql - > ', e)

    baseball_solution.to_csv(path_to_new_csv)


path_to_csv = './data/baseballdatabank-2017.1/core/Master.csv'
path_to_new_csv = './queriedData.csv'

query_data(path_to_csv, path_to_new_csv)
