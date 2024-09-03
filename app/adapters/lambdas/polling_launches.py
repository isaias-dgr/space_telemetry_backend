import logging
# from app.usescase.polling_telemetry import PollingTelemetry
from app.domain.launches import Launch


def lambda_handler(event, context):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Polling Launches")
    l = Launch()

    return {
        "statusCode": 200,
        "body": {
            "message": "Not Found",
            "import": "polling_telemetry.get_and_save_launches()",
        },
    }
