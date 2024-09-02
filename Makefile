COMPOSE_FILE=docker-compose.yml
AWS_COMMAND=aws --profile localstack-profile --endpoint-url=http://localhost:4566

.PHONY: up down restart logs logs-app logs-db logs-redis logs-swagger ps clean

up:
	@docker-compose -f $(COMPOSE_FILE) up --build -d

down:
	@docker-compose -f $(COMPOSE_FILE) down

restart:
	@docker-compose -f $(COMPOSE_FILE) down
	@docker-compose -f $(COMPOSE_FILE) up --build

logs:
	@docker-compose -f $(COMPOSE_FILE) logs -f

logs-app:
	@docker-compose -f $(COMPOSE_FILE) logs -f app

logs-db:
	@docker-compose -f $(COMPOSE_FILE) logs -f db

logs-redis:
	@docker-compose -f $(COMPOSE_FILE) logs -f redis

logs-swagger:
	@docker-compose -f $(COMPOSE_FILE) logs -f swagger

ps:
	@docker-compose -f $(COMPOSE_FILE) ps

clean:
	@docker-compose -f $(COMPOSE_FILE) down -v
	@docker system prune -f

test:
	@docker-compose -f $(COMPOSE_FILE) run --rm tests
