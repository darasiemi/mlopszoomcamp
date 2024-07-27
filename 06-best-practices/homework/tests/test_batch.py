import os
import sys
import boto3


# sys.path.append('../')  # Add the parent directory to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

import pandas as pd
from batch import prepare_data
from datetime import datetime

def get_input_path(year, month):
    default_input_pattern = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    input_pattern = os.getenv('INPUT_FILE_PATTERN', default_input_pattern)
    return input_pattern.format(year=year, month=month)

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]
    year = 2023
    month = 1
    input_file = get_input_path(year, month)
    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)

    S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
    
    options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
       }
    }
    print(input_file)
    # Save the DataFrame to S3
    df.to_parquet(
        input_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )
    # print(df)
    categorical = ['PULocationID', 'DOLocationID']
    result_df = prepare_data(df, categorical)
    print(result_df.info())

    print(result_df[columns])

    # Expected output
    expected_data = [
        (str(-1), str(-1), dt(1, 1), dt(1, 10)),
        (str(1), str(1), dt(1, 2), dt(1, 10)),
    ]
    expected_df = pd.DataFrame(expected_data, columns=columns)
    
    # Assert
    pd.testing.assert_frame_equal(result_df[columns].reset_index(drop=True), expected_df.reset_index(drop=True))

if __name__ == "__main__":
    test_prepare_data()
    print("All tests passed.")
