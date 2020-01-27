DOCKER_TAG ?= mytinyurl

.PHONY: run
run: build
	docker run -d -p 127.0.0.1:23456:8888 -v ~/container_storage/urls:/tmp --name $(DOCKER_TAG)-container $(DOCKER_TAG)


.PHONY: run-dev
run-dev: build
	docker run --rm -it -p 23456:8888 -v ~/container_storage/urls:/tmp --name $(DOCKER_TAG)-container $(DOCKER_TAG)


.PHONY: build
build:
	docker build -t $(DOCKER_TAG) .
