.PHONY: build
build:	## Build project with compose
	docker-compose up --build --remove-orphans -d

.PHONY: up
up:	## Run project with compose
	docker-compose up -d

.PHONY: stop
stop: ## Stop project containers with compose
	docker-compose down

.PHONY: down
down: ## Reset project containers with compose
	docker-compose down -v --remove-orphans

