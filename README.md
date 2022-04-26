
<h1 align="center">Movie Recommendation Challenge</h1>
<p align="center">
  <img src="https://img.shields.io/badge/python-3.8-blue" />
  <img src="https://img.shields.io/badge/coverage-82%25-green" />
  <a href="https://www.linkedin.com/in/erickseo/">
  <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?&style=flat-square&logo=linkedin&logoColor=white">
  </a>
  <a href="https://github.com/seoerick">
  <img src="https://img.shields.io/badge/GitHub-000000?&style=flat-square&logo=GitHub&logoColor=white">
  </a>
  <a href="mailto:erick.seo@picpay.com" alt="gmail" target="_blank">
  <img src="https://img.shields.io/badge/-Gmail-FF0000?style=flat-square&labelColor=FF0000&logo=gmail&logoColor=white&link=mailto:erick.seo@picpay.com" />
  </a>
  </br>

  ![<img src="static/neighbor.jpeg" width="100"/>](static/neighbor.jpeg)

</p>



## Usage

![<img src="static/make.png" width="100"/>](static/make.png)

To download dataset and cleaning:

```
make cleaning_process
```

To training yout KNN dataset:

```
make training_process
```

To launch movie_recommender endpoint:

```
make build_endpoint
```

To build all:
```
make build
```

To execute unit_test:
```
make unit_test
```

## Endpoints

![<img src="static/similar.png" width="100"/>](static/similar.png)

### List Movies
list movieId and Title available
```
curl --location --request GET 'http://0.0.0.0:5005/list_movie'
```

### Simmilar Movies
list the 10 most similar movies
```
curl --location --request GET 'http://0.0.0.0:5005/similar_movie?movieId=1'
```


## ToDo
- Swagger
- Code organization
- Optimize Cleaning process (memory) with tags
- levenshtein distance
- Add new ratings movies endpoint
- Airflow pipeline process
