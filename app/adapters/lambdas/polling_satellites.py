import logging
from app.usescase.polling_satellites import PollingSatellite
from app.adapters.services.spacex import SpaceXService
from app.adapters.repositories.elasticsearch.satellite_repository import (
    SatelliteStore,
)


def lambda_handler(event, context):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    space_service = SpaceXService("https://api.spacexdata.com")
    telemetry_store = SatelliteStore("http://elasticsearch", "9200")

    usecase_satellite = PollingSatellite(space_service, telemetry_store)
    total = usecase_satellite.get_and_save_satellites()
    logging.info(f"Total satellites: {total}")
    return {
        "statusCode": 200,
        "body": {"message": "success", "total": total},
    }
