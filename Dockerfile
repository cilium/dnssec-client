FROM python:alpine3.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk add g++ && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del g++

COPY . .

ENTRYPOINT [ "python", "./client.py" ]
