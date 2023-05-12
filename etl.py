import pandas as pd
import logging
import os
from sqlalchemy import create_engine

# Set up logging
logging.basicConfig(level=logging.INFO, filename='etl.log')

def extract(filename):
    logging.info(f'Extracting data from {filename}')
    try:
        data = pd.read_csv(filename)
        logging.info(f'Successfully extracted data from {filename}')
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        raise
    return data

def transform(data, columns):
    logging.info('Transforming data')
    try:
        # Rename columns
        data = data.rename(columns=columns)
        # Clean up missing data
        data = data.dropna()
        logging.info('Successfully transformed data')
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        raise
    return data

def load(data, database_uri, table_name):
    logging.info(f'Loading data into {table_name}')
    try:
        engine = create_engine(database_uri)
        data.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f'Successfully loaded data into {table_name}')
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        raise

def run_etl(filename, columns, database_uri, table_name):
    data = extract(filename)
    data = transform(data, columns)
    load(data, database_uri, table_name)

if __name__ == '__main__':
    filename = os.getenv('DATA_FILENAME')
    columns = {'old_name': 'new_name'}
    database_uri = os.getenv('DATABASE_URI')
    table_name = os.getenv('TABLE_NAME')
    run_etl(filename, columns, database_uri, table_name)
