import boto3
from botocore.exceptions import ClientError
from typing import Optional
from app.domain.rockets import Rocket
from app.domain import convert_floats_to_decimal
from app.ports.rockets_storage import RocketRepository


class RocketRepository(RocketRepository):
    def __init__(self, table_name: str = "Rockets"):
        self.table_name = table_name
        self.dynamodb = boto3.resource("dynamodb")
        self.table = self.dynamodb.Table(table_name)

    def add(self, rocket: Rocket) -> Rocket:
        try:
            rocket_dict = rocket.to_dict()
            rocket_item = convert_floats_to_decimal(rocket_dict)
            self.table.put_item(Item=rocket_item)
            return rocket
        except ClientError as e:
            # Handle exception
            return None

    def get(self, rocket_id: int) -> Optional[Rocket]:
        try:
            response = self.table.get_item(Key={"rocket_id": rocket_id})
            item = response.get("Item")
            if item:
                return Rocket.from_dict(item)
            else:
                return None
        except ClientError as e:
            # Handle exception
            return None

    def update(self, rocket_id: int, name: str, description: str) -> Optional[Rocket]:
        try:
            response = self.table.update_item(
                Key={"rocket_id": rocket_id},
                UpdateExpression="SET #n = :name, #d = :description",
                ExpressionAttributeNames={"#n": "name", "#d": "description"},
                ExpressionAttributeValues={":name": name, ":description": description},
                ReturnValues="ALL_NEW",
            )
            item = response.get("Attributes")
            if item:
                return Rocket.from_dict(item)
            else:
                return None
        except ClientError as e:
            # Handle exception
            return None

    def delete(self, rocket_id: int) -> bool:
        try:
            self.table.delete_item(Key={"rocket_id": rocket_id})
            return True
        except ClientError as e:
            # Handle exception
            return False
