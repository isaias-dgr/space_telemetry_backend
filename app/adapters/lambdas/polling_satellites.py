import logging
from app.usescase.polling_satellite import PollingSatellite
from app.adapters.services.spacex import SpaceXService
from app.adapters.repositories.elasticsearch.telemetry_repository import (
    SatelliteStore,
)


def lambda_handler(event, context):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    space_service = SpaceXService("https://api.spacexdata.com")
    telemetry_store = SatelliteStore("http://elasticsearch", "9200")

    p = PollingSatellite(space_service, telemetry_store)
    total = p.get_and_save_launches()

    return {
        "statusCode": 200,
        "body": {"message": "success", "total": total},
    }
