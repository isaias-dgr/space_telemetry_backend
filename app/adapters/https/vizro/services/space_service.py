from app.adapters.https.vizro.utils import singleton
import httpx
from enum import Enum


class SpaceData(Enum):
    AVERAGE_THRUST = "average_thrust"
    CLIENT_DISTRIBUTION = "client_distribution"
    COST_COMPARISON_BY_ROCKET_TYPE = "cost_comparison_by_rocket_type"
    COST_PER_LAUNCH_AVG = "cost_per_launch_avg"
    ENGINE_COUNT_AVG = "engine_count_avg"
    LAUNCH_ORBITS = "launch_orbits"
    LAUNCH_SUCCESS_RATE = "launch_success_rate"
    LAUNCHES_PER_YEAR = "launches_per_year"
    PAYLOAD_WEIGHT_AVG = "payload_weight_avg"
    REUSABILITY_COUNT = "reusability_count"
    STAGE_BURN_TIME_AVG = "stage_burn_time_avg"
    SUCCESS_RATE_BY_ROCKET_TYPE = "success_rate_by_rocket_type"

SINGLES_VALUES = [
    "average_thrust",
    "cost_per_launch_avg",
    "engine_count_avg",
    "payload_weight_avg",
    "stage_burn_time_avg",
]

PIE_VALUES = [
    "client_distribution",
    "cost_comparison_by_rocket_type",
    "launch_orbits", 
    "reusability_count",
    "launch_success_rate"
]

HISTOGRAM_VALUES = ["launches_per_year"]

BINARI_VALUES = [
    "reusability_count",
]

BAR_VALUES = ["launches_per_year"]

@singleton
class SpaceService:

    def __init__(self):
        self.__url = "http://0.0.0.0:8000/dashboard"
        response = httpx.get(self.__url)
        if response.status_code == 200:
           self.__data = response.json().get("data", {})
        else:
            raise Exception(f"Failed to get satellite. Status code: {response.status_code}")
        
    def get_data(self, data_type: SpaceData):
        if data_type.value in SINGLES_VALUES:
            return str(self.__data[data_type.value]["value"])
        return "0"
    
    def get_label_values(self, data_type: SpaceData):
        labels, values = [], []
        for item in self.__data[data_type.value]["buckets"]:
            values.append(item["key"])
            labels.append(item["doc_count"])
        return (labels,values)

    def get_histogram_values(self, data_type: SpaceData):
        labels, values = [], []
        for item in self.__data[data_type.value]["buckets"]:
            year = item["key_as_string"].split("-")[0]
            labels.append(year)
            values.append(item["doc_count"])
        return (labels,values)
    