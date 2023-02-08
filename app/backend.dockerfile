FROM tiangolo/uvicorn-gunicorn:python3.10-slim

WORKDIR /src
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/src

COPY scripts/start-server.sh /src/start-server.sh

## install dependencies
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src/

EXPOSE 8000
