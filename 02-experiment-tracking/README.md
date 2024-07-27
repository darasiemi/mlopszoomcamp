Data scientists and machine learning professionals often perform several experiments, which can be difficult to track. In the data engineering zoomcamp this week, I learnt how to track machine learning experiments using MLFlow.

As the name suggests, experiment tracking is the process of keeping track of all relevant information such as source code, environment, data, model, hyperparameters, metrics, etc, from a Machine Learning experiment.

This drives reproducibility, organization and optimization. Apart from MLflow, there are other tools that can be used for this such as Weights and Biases, Neptune AI etc.

In MLflow, experiments are organized into runs and the runs keep track of parameters, metrics, metadata, artifacts, models, etc.

I experimented with MLflow by creating a separate Conda environment for this week. I tried out different methods of experiment tracking namely:locally, using a tracking server and logging the experiments on AWS for easy collaboration. Saving the model artificacts on AWS allows teams to collaborate seamlessly.

Finally, I also experimented  with hyper-parameter tuning on MLflow. I particularly enjoyed this week’s task because I got to play around with AWS. It was fun!

Instructions on reproducing this modules is as follows:

To create environment
```bash
conda create -n exp-tracking-env python=3.9
```
To launch environment
```bash
conda activate exp-tracking-env
```
To install dependencies
```bash
pip install -r requirements.txt
```
To launch mlflow
```bash 
mlflow ui --backend-store-uri sqlite:///mlflow.db
```
To run preprocess_data.py:
```bash
python preprocess_data.py --raw_data_path /home/ubuntu/data --dest_path artfifacts/
```



