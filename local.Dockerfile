FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN apt-get update && \
    apt-get install curl -y


ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PATH_MODEL=/movie_recommendation/models
ENV DATASET_TRAIN_MODEL="/$PATH_MODEL/movie.parquet"
ENV CATEGORY_PKL="/$PATH_MODEL/category.pickle"
RUN python3 -m venv $VIRTUAL_ENV

RUN python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt && \
    python3 setup.py install

RUN groupadd knn --gid 1000 && \
    useradd knn --uid 1000 --gid 1000 && \
    chown -R "knn:knn" /movie_recommendation

USER knn:knn
EXPOSE 5005

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
