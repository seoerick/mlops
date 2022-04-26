FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app

RUN apt-get update && \
    apt-get install curl -y && \
    apt-get install unzip

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PATH_MODEL=models
ENV DATASET_TRAIN_MODEL="$PATH_MODEL/movie.parquet"
ENV CATALOG_PKL="$PATH_MODEL/catalog.pickle"


RUN python3 -m venv $VIRTUAL_ENV

RUN python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt && \
    python3 setup.py install

RUN groupadd knn --gid 1000 && \
    useradd knn --uid 1000 --gid 1000 && \
    chown -R "knn:knn" movie_recommendation

USER knn:knn
EXPOSE 5005


WORKDIR /app/movie_recommendation
ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
