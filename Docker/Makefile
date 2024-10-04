# Variables
DATA_DIR = data
DB_DIR = ${DATA_DIR}/db
SUB_DIR = ${DATA_DIR}/subject

# Macros
DOCKER_COMPOSE = docker compose
DC_RUN_DB = run --rm db sh -c
DC_RUN_APP = run --rm python sh -c

all: build

# Target to create directories
create-dirs:
	@echo "Creating directories..." 
	@mkdir -p $(DB_DIR) $(SUB_DIR)

# Target to download official Docker images
pull-images:
	@docker pull python:3.12.4-alpine3.19
	@docker pull postgres:13-alpine

# DEBUG

build: create-dirs pull-images
	@echo "Building Docker images..."
	@$(DOCKER_COMPOSE) build

up:
	@echo "Running setup tasks..."
	@$(DOCKER_COMPOSE) up

status: 
	@echo "Control status app..."
	@$(DOCKER_COMPOSE) ps

down:
	@echo "Turning off everything."
	@$(DOCKER_COMPOSE) down

clean: down
	@echo "Cleaning up data directories..."
	@$(DOCKER_COMPOSE) $(DC_RUN_DB) "rm -rf var/lib/postgresql/data/*"
	@echo "Data and log directories cleaned."

fclean: clean
	@echo "Deleting all Docker resources..."
	@rm -rf $(DB_DIR) $(SUB_DIR)
# @docker image rm src-app
	@docker volume rm docker_db-data
	@docker image rm docker-python
#	@docker-compose down --rmi all --volumes --remove-orphans
	@echo "Deleted containers, images, and volumes."
	
re: fclean all
