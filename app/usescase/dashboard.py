from app.ports.satellite_storage import SatelliteStoreService
from app.ports.telemetry_storage import TelemetryStoreService


class Dashboard:
    def __init__(
        self, telemetry_store: TelemetryStoreService,
        satellite_store: SatelliteStoreService
    ):
        self.telemetry_store = telemetry_store
        self.satellite_store = satellite_store


    def get_dashboard(self):
        data =  self.telemetry_store.get_dashboard()
        return {"data": data.to_dict()}
        
