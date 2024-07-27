This week on the MLOps Zoomcamp, I learnt how to monitor machine learning(ML) models in production. Model monitoring is necessary because over time, ML models can degrade. Metrics usually monitored are model performance, data drift, concept drift, etc.

Apart from model and data drift monitoring, the service health such as uptime, latency can also be monitored. Furthermore, data quality and integrity metrics such as share of missing data, counts, value range, etc are also monitored.

In sensitive applications like those that involve humans, one would also want to monitor model bias.

I also learnt that how we deploy models influence how we monitor the model. ML monitoring can be done by adding ML metrics to service health monitoring (e.g in Grafana), or a custom ML-focused Dashboard can be built for it.

Generally, as discussed last week, there are two ways of deploying models: batch and online. For batch models, one can monitor metrics such as the expected data quality, data distribution type, descriptive statistics, etc.

Likewise, for non-batch models, similar metrics such as descriptive statistics and quality are monitored. To monitor data drift in non-batch models, it is advised to select a window, so as to compute the data being processed in batches, for subsequent monitoring.

This week, I was able to implement machine learning service for prediction, and the prediction logs were saved in a database. The validation data was also saved as a reference data. When a prediction is made on a new data, this is compared with the reference data.

Finally, reports for the model monitoring are generated using Evidently AI and dashboards are also created using Grafana.

Instructions to reproduce this code are as follows:

Create Conda environment `conda create -n py11 python=3.11`

Activate environment `conda activate py11`

Install required packages `pip install -r requirements.txt`

To build container`docker-compose up --build`

To fix Attribute error `python -m pip install numpy==1.26.4`