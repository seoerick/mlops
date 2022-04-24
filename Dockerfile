FROM python:3.7-alpine
WORKDIR /app
COPY . /app

RUN groupadd knn --gid 1000 && \
    useradd knn --uid 1000 --gid 1000 && \
    chown -R "knn:knn" /app

RUN apt-get update && \
    apt-get install curl -y && \
    python3 -m pip install --upgrade pip && \
    python3 -m venv env && \
    source env/bin/activate && \
    pip3 install gunicorn && \
    pip3 install -r requirements.txt && \
    python3 setup.py install

USER knn:knn
EXPOSE 5003

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
