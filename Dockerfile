# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.6

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.
#RUN apt-get update && apt-get install -y supervisor
#RUN apt-get install redis-server
COPY requirements.txt .
RUN pip uninstall -y tensorflow
RUN pip install tensorflow==1.14
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install redis-server
RUN service redis-server start
RUN python test.py

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

EXPOSE 8080
# needs to be set else Celery gives an error (because docker runs commands inside container as root)
#ENV C_FORCE_ROOT=1

# run supervisord
#CMD ["supervisord"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080",  "--workers", "1", "--threads", "8", "app:app", "--timeout", "900"]
