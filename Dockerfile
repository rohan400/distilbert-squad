# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.6.8

# Copy local code to the container image.
ENV APP_HOME /app
ENV APP_HOME /app/model
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.

COPY requirements.txt .
RUN pip uninstall -y tensorflow
RUN pip install tensorflow
RUN pip install -r requirements.txt
RUN pip install torch
RUN apt-get update
#RUN apt-get -y install redis-server
#RUN service redis-server start
#RUN apt-get install -y supervisor
RUN python test.py



EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080",  "--workers", "1", "--threads", "8", "app:app", "--timeout", "900"]
