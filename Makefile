IMAGE := knn
VERSION:= $(shell grep -m 1 '__version__' setup.py | cut -d '=' -f 2 | tr -d "'" | tr -d '[:space:]')

.PHONY: clean
clean:
	find . -name \*.pyc -delete
	find . -name __pycache__ -delete	
	find . -name .coverage -delete
	find . -name sessions.db -delete
	find . -name coverage.xml -delete
	find . -name pytestdebug.log -delete
	find .pytest_cache -delete || true

	rm -rf dist/

.PHONY: test_unit
test_unit:
	python3 -bb -m pytest tests

.PHONY: lint
lint:
	flake8 .

.PHONY: mypy
mypy:
	mypy --ignore-missing-imports --strict-optional --warn-no-return .

.PHONY: test
test: test_unit lint mypy

.PHONY: build
build:
	docker rmi -f ${IMAGE}:latest || true
	docker rmi -f ${IMAGE}:${VERSION} || true
	docker rm ${IMAGE} || true
	docker build -f local.Dockerfile -t ${IMAGE}:${VERSION} .
	docker tag ${IMAGE}:${VERSION} ${IMAGE}:latest
	docker build -t ${IMAGE} . -f local.Dockerfile
	docker run --name ${IMAGE} --publish 5005:5005 ${IMAGE}


.PHONY: push-image
push-image:
	docker push ${IMAGE}:${VERSION}
	docker push ${IMAGE}:latest

.PHONY: build-push-image
build-push-image: build push-image

.PHONY: requirements
requirements:
	python -m pip install -r requirements_test.txt
	python -m pip install -r requirements.txt

test:
	pytest --cov=quality_service --cov-report term-missing --ignore=setup.py

.PHONY: coverage
coverage:
	coverage run --source quality_service -m pytest --debug 
	coverage report -m
	coverage xml
