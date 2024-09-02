import logging
from app.usescase.polling_telemetry import PollingTelemetry


def lambda_handler(event, context):
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Log a message
    logging.info("Polling Launches")
    polling_telemetry = PollingTelemetry()

    return {
        "statusCode": 200,
        "body": {
            "message": "Not Found",
            "import": polling_telemetry.get_and_save_launches(),
        },
    }
