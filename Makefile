DOCKER_TAG ?= mytinyurl

.PHONY: run
run: build
	docker run -d -p 127.0.0.1:9999:8888 --name $(DOCKER_TAG)-container $(DOCKER_TAG)

.PHONY: run-dev
run-dev: build
	docker run --rm -it -p 9999:8888 --name $(DOCKER_TAG)-container $(DOCKER_TAG)

.PHONY: build
build:
	docker build -t $(DOCKER_TAG) .



