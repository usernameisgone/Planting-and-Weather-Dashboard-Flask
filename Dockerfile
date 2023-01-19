# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN python -m pip install gunicorn

WORKDIR /Planting_and_Weather_Dashboard___Flask
ADD . /Planting_and_Weather_Dashboard___Flask/

ENV FLASK_APP=Planting_and_Weather_Dashboard___Flask
ENV FLASK_ENV=production
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD flask run --host 0.0.0.0

EXPOSE 5000

