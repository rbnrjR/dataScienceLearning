import pandas as pd


def add_full_name(path_to_csv, path_to_new_csv):
    # creates a pandas dataframe from the csv
    baseball_data = pd.read_csv(path_to_csv)

    # creating a new column to the dataframe
    baseball_data['fullName'] = baseball_data['nameFirst'] + \
        ' ' + baseball_data['nameLast']

    # writing the data to the new csv file
    baseball_data.to_csv(path_to_new_csv)

    print('Written to the destination csv')


path_to_csv = './data/baseballdatabank-2017.1/core/Master.csv'
path_to_new_csv = './master.csv'


add_full_name(path_to_csv, path_to_new_csv)
