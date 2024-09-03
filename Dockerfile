FROM python:3.12-alpine AS builder
RUN apk add --no-cache gcc musl-dev libffi-dev libpq-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache entr
COPY . . 

FROM python:3.12-alpine AS development
RUN apk add --no-cache bash entr
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY requirements_dev.txt .
RUN pip install --no-cache-dir -r requirements_dev.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM python:3.12-alpine AS production
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.12-alpine AS test
RUN apk add --no-cache bash entr
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .
CMD ["sh", "-c", "find . -name '*.py' | entr -r -n pytest"]

FROM python:3.12-alpine AS lambda_builder
RUN apk add --no-cache gcc musl-dev libffi-dev libpq-dev zip
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN zip -r lambda_package.zip . && \
    mkdir -p /out && \
    mv lambda_package.zip /out/
COPY . /out

FROM amazon/aws-lambda-python:3.12 AS lambda_runtime
WORKDIR /var/task
COPY --from=lambda_builder /out/lambda_package.zip .
CMD ["app.adapters.lambdas.polling_launches.lambda_handler"]