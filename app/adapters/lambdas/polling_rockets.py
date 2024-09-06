import logging
from app.usescase.polling_rockets import PollingRocket
from app.adapters.services.spacex import SpaceXService
from app.adapters.repositories.dynamodb.rocket_repository import (
    RocketRepository,
)


def lambda_handler(event, context):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    space_service = SpaceXService("https://api.spacexdata.com")
    telemetry_store = RocketRepository()

    usecase_rocket = PollingRocket(space_service, telemetry_store)
    total = usecase_rocket.get_and_save_rockets()
    logging.info(f"Total rockets: {total}")
    return {
        "statusCode": 200,
        "body": {"message": "success", "total": total},
    }
