COMPOSE_FILE=docker-compose.yml
AWS_COMMAND=aws --profile localstack-profile --endpoint-url=http://localhost:4566
CURRENT_DIR := $(shell pwd)

.PHONY: up down restart logs logs-app logs-db logs-redis logs-swagger ps clean

up:
	@docker-compose -f $(COMPOSE_FILE) up --build app -d

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
	lambda-runtime:

create-package:
	@echo "Creating package zip"
	@pip install -qr requirements.txt -t ./package
	@cd package && zip -rq9 ${CURRENT_DIR}/function.zip .
	@cd ${CURRENT_DIR} && zip -gqr function.zip app/

create-lambda: create-package
	@echo "Creating lambda function"
	@$(AWS_COMMAND) lambda create-function \
		--function-name polling_lambda \
		--runtime python3.12 \
		--handler app.adapters.lambdas.polling_launches.lambda_handler \
		--zip-file fileb://function.zip \
		--role arn:aws:iam::123456789012:role/lambda-role 
	@rm -rf package function.zip

invoke-lambda:
	@$(AWS_COMMAND) lambda invoke \
		--function-name polling_lambda  \
		--log-type Tail \
		output.json \
		--query 'LogResult' \
		--output text | base64 -d 
	@jq . output.json
	@rm output.json

invoke-create-lambda: update-lambda
	@$(AWS_COMMAND) lambda invoke \
		--function-name polling_lambda  \
		--log-type Tail \
		output.json \
		--query 'LogResult' \
		--output text | base64 -d 
	@jq . output.json
	@rm output.json

delete-lambda:
	@$(AWS_COMMAND) lambda delete-function \
		--function-name polling_lambda

update-lambda:create-package
	@echo "Updating lambda function"
	@$(AWS_COMMAND) lambda update-function-code \
		--function-name polling_lambda \
		--zip-file fileb://function.zip
	@rm -rf package function.zip