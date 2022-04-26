IMAGE := knn
VERSION:= $(shell grep -m 1 '__version__' setup.py | cut -d '=' -f 2 | tr -d "'" | tr -d '[:space:]')

lint:
	black movie_recommendation
	autoflake -r -i movie_recommendation

requirements:
	python -m pip install -r requirements_test.txt
	python -m pip install -r requirements.txt

unit_test:
	pytest --cov=movie_recommendation --cov-report term-missing --ignore=setup.py -vv

cleaning_process:
	sh download_movie_lens.sh
	time python3 data_process/cleaning.py data_process/cfg/cleaning.yaml

training_process:
	time python3 data_process/training.py data_process/cfg/training.yaml

build_endpoint:
	docker rmi -f ${IMAGE}:latest || true
	docker rmi -f ${IMAGE}:${VERSION} || true
	docker rm ${IMAGE} || true
	docker build -f local.Dockerfile -t ${IMAGE}:${VERSION} .
	docker tag ${IMAGE}:${VERSION} ${IMAGE}:latest
	docker build -t ${IMAGE} . -f local.Dockerfile
	docker run --name ${IMAGE} --publish 5005:5005 ${IMAGE}


build:
	make cleaning_process
	make training_process
	make build_endpoint


coverage:
	coverage run --source quality_service -m pytest --debug 
	coverage report -m
	coverage xml
