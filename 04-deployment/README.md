I have always been curious on how the many machine learning (ML) models I have trained on Jupyter notebooks can be deployed for real-life applications. This is one of my biggest inspirations for joining the MLOps zoomcamp and I am glad this desire was met this week.

This week, I learnt how to deploy an ML model for taxi ride duration prediction. There are two different types of model deployments: batch and online. In batch (also know as offline), predictions are pre-computed in batches at regular intervals. This can be hourly, weekly etc.

The batch deployment works by pulling data from a database, while a job is scheduled to run the model on this data. It then sends the predictions to a database, which can be further used. An example of an application where batch is relevant is churn prediction.

For online deployment, the model makes predictions instantaneously. The model is up and running always. Online deployment can be further divided into web service and streaming.

Web service is a common way of deploying models. This makes the ML model accessible to other applications via HTTP requests. For example, a mobile app can be connected to a backend which communicates with a web service that runs an ML model. This is a one to one relationship.

Streaming involves producers and consumers, where the producers produces events while consumers read from that stream and act on it. This is usually a one to many or many to many relationship.

There is usually no explicit connection between the producers and consumers in streaming. An example of streaming deployment will be social media moderation, and a use case of YouTube was made in the course.

I was able to implement all modes of model deployment. Tools I used are: REST API using Flask for web-service, docker for containerizing my applications, AWS Lambda and Kinesis for streaming deployment, MLflow, amongst others.


Below are the instructions to reproduce the code:

To configure pip environment with packages
```bash
pipenv install scikit-learn==1.2.2 flask --python=3.11
```

To launch shell
```bash
pipenv shell
```

To copy model
```bash
cp /home/ubuntu/mlopszoomcamp/01-intro/models/lin_reg.bin .
```

To install gunicorn for deployment in production server
```bash
pipenv install gunicorn
```

To deploy app in production server
```bash
gunicorn --bind=0.0.0.0:9696 predict:app
```

To install requests for development
```bash
pipenv install --dev requests
```

To build docker image
```bash
docker build -t ride-duration-prediction-service:v1 .
```

To run docker container
```bash
docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1
```
