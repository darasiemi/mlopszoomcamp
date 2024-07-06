To create environment
`conda create -n exp-tracking-env python=3.9`
To launch environment
`conda activate exp-tracking-env`
To install dependencies
`pip install -r requirements.txt`
To launch mlflow
` mlflow ui --backend-store-uri sqlite:///mlflow.db`
To run preprocess_data.py:
`python preprocess_data.py --raw_data_path /home/ubuntu/data --dest_path artfifacts/`


