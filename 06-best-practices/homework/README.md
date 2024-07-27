To run python script
```bash
python batch.py 2023 03
```

To create test environment
```bash
pipenv install --dev pytest
```

To create s3 using localstack
```bash
aws s3 mb s3://nyc-duration --endpoint-url=http://localhost:4566
```

To check list of s3 in localstack
```bash
aws s3 ls --endpoint-url=http://localhost:4566
```

To set environment variables
```bash
export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
```
To move files from local machine to s3 in localstack
```bash
aws --endpoint-url=http://localhost:4566 s3 cp data/yellow_tripdata_2023-03.parquet $INPUT_FILE_PATTERN
```
To check if the file was created in s3
```bash
aws --endpoint-url=http://localhost:4566 s3 ls s3://nyc-duration/in/ 
```

To set environment variable
```bash
export S3_ENDPOINT_URL="http://localhost:4566"
```