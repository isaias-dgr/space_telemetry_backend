import logging
from app.usescase.polling_telemetry import PollingTelemetry
from app.adapters.services.spacex import SpaceXService
from app.adapters.repositories.elasticsearch.telemetry_repository import (
    TelemetryStore,
)

def lambda_handler(event, context):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    space_service = SpaceXService("https://api.spacexdata.com")
    telemetry_store = TelemetryStore("http://elasticsearch", "9200")

    usecase_telemetry = PollingTelemetry(space_service, telemetry_store)
    total = usecase_telemetry.get_and_save_launches()
    logging.info(f"Total launches: {total}")
    return {
        "statusCode": 200,
        "body": {"message": "success", "total": total},
    }
