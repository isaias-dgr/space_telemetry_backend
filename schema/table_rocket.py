import boto3
import os


def create_dynamo_table():
    env = os.environ.get("ENV", "local")
    dynamodb = None
    if env == "local":
        dynamodb = boto3.client(
            "dynamodb",
            endpoint_url="http://localhost:4566",
            region_name="us-east-1",
            aws_access_key_id="dummy",
            aws_secret_access_key="dummy",
        )
    else:
        dynamodb = boto3.client("dynamodb", region_name="us-east-1")

    table = dynamodb.create_table(
        TableName="Rockets",
        KeySchema=[{"AttributeName": "name", "KeyType": "HASH"}],
        AttributeDefinitions=[
            {"AttributeName": "name", "AttributeType": "S"}
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )


    print("Creando la tabla...")
    dynamodb.get_waiter("table_exists").wait(TableName="Rockets")
    print("Tabla 'Rockets' creada con éxito.")


if __name__ == "__main__":
    create_dynamo_table()
