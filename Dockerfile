FROM python:3.10-alpine AS builder
RUN apk add --no-cache gcc musl-dev libffi-dev libpq-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache entr
COPY . . 

FROM python:3.10-alpine AS development
RUN apk add --no-cache bash entr
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY requirements_dev.txt .
RUN pip install --no-cache-dir -r requirements_dev.txt
COPY . .
EXPOSE 8000
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
CMD ["gunicorn", "-w", "4", "--access-logfile", "-", "--error-logfile", "-", "--reload", "--bind", "0.0.0.0:8000", "app.main:app"]

FROM python:3.10-alpine AS front-development
RUN apk add --no-cache bash entr
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY requirements_dev.txt .
COPY . .
EXPOSE 8050
CMD ["python", "app/adapters/https/vizro/main.py"]

FROM python:3.10-alpine AS production
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10-alpine AS test
RUN apk add --no-cache bash entr
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .
CMD ["sh", "-c", "find . -name '*.py' | entr -r -n pytest"]

FROM amazonlinux:2 AS build_lambda
RUN yum install -y zip
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt -t .
RUN zip -r lambda_function.zip .
CMD ["cp", "lambda_function.zip", "/out/lambda_function.zip"]

