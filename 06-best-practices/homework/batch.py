#!/usr/bin/env python
# coding: utf-8
import os
import sys
import pickle
import pandas as pd

with open('model.bin', 'rb') as f_in:
    dv, lr = pickle.load(f_in)

categorical = ['PULocationID', 'DOLocationID']

def get_input_path(year, month):
    default_input_pattern = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    input_pattern = os.getenv('INPUT_FILE_PATTERN', default_input_pattern)
    return input_pattern.format(year=year, month=month)


def get_output_path(year, month):
    default_output_pattern = 's3://nyc-duration/taxi_type=fhv/year={year:04d}/month={month:02d}/predictions.parquet'
    output_pattern = os.getenv('OUTPUT_FILE_PATTERN', default_output_pattern)
    return output_pattern.format(year=year, month=month)

def read_data(filename):
    S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')

    options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
       }
    }

    if S3_ENDPOINT_URL:
        df = pd.read_parquet(filename, storage_options=options)
        return df
    df = pd.read_parquet(filename)
    return df

def prepare_data(df, categorical):
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df
def save_data(df, output_file):
    S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')

    options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
       }
    }

    df.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
    )

def main(categorical, year, month):
    input_file = get_input_path(year, month)
    output_file = get_output_path(year, month)

    df = read_data(input_file)
    df = prepare_data(df, categorical)
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)

    print('predicted mean duration:', y_pred.mean())

    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred

    # df_result.to_parquet(output_file, engine='pyarrow', index=False)
    save_data(df_result,output_file )

    # Read the output DataFrame from S3
    df_output = read_data(output_file)

    # Calculate the sum of predicted durations
    sum_predicted_durations = df_output['predicted_duration'].sum()

    print("Sum of predicted durations:", sum_predicted_durations)

if __name__ == "__main__":
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f'output/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    main(categorical, year, month)
