# Variables
COMPOSE_FILE=docker-compose.yml

# Default target
.PHONY: up
up:
    docker-compose -f $(COMPOSE_FILE) up --build -d

.PHONY: down
down:
    docker-compose -f $(COMPOSE_FILE) down

.PHONY: restart
restart:
    docker-compose -f $(COMPOSE_FILE) down
    docker-compose -f $(COMPOSE_FILE) up --build

.PHONY: logs
logs:
    docker-compose -f $(COMPOSE_FILE) logs -f

.PHONY: logs-app
logs-app:
    docker-compose -f $(COMPOSE_FILE) logs -f app

.PHONY: logs-db
logs-db:
    docker-compose -f $(COMPOSE_FILE) logs -f db

.PHONY: logs-redis
logs-redis:
    docker-compose -f $(COMPOSE_FILE) logs -f redis

.PHONY: logs-swagger
logs-swagger:
    docker-compose -f $(COMPOSE_FILE) logs -f swagger

.PHONY: ps
ps:
    docker-compose -f $(COMPOSE_FILE) ps

.PHONY: clean
clean:
    docker-compose -f $(COMPOSE_FILE) down -v
    docker system prune -f