from typing import Dict, Any, List
from app.adapters.repositories.elasticsearch.repository import ElasticStore
from app.domain.dashboard import Dashboard
from app.domain.utils import from_dict
from app.ports.telemetry_storage import TelemetryStoreService


class TelemetryStore(
    ElasticStore,
    TelemetryStoreService,
):

    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.index = "telemetry"

    def add(self, document: Dict[str, Any]) -> None:
        super().add(self.index, document)

    def add_bulk(self, documents: List[Dict[str, Any]]) -> None:
        super().add_bulk(self.index, documents)

    def get_dashboard(self) -> Dashboard:
        query = {
            "_source": ["rocket.country", "payloads.customers", "payloads.name",
                        "payloads.type", "payloads.orbit", "payloads.reference_system",
                        "payload.regime",  "rocket.name", "rocket.id", "rocket.company"],
            "size": 0,
            "aggs": {
                "launch_success_rate": {
                    "terms": {
                        "field": "success",
                        "size": 2
                    }
                },
                "cost_per_launch_avg": {
                    "avg": {
                        "field": "rocket.cost_per_launch"
                    }
                },
                "launch_orbits": {
                    "terms": {
                        "field": "payloads.orbit.keyword"
                    }
                },
                "average_thrust": {
                    "avg": {
                        "field": "rocket.first_stage.thrust_sea_level.kN"
                    }
                },
                "engine_count_avg": {
                    "avg": {
                        "field": "rocket.engines.number"
                    }
                },
                "reusability_count": {
                    "terms": {
                        "field": "rocket.first_stage.reusable"
                    }
                },
                "payload_weight_avg": {
                    "avg": {
                        "field": "payloads.mass_kg"
                    }
                },
                "client_distribution": {
                    "terms": {
                        "field": "payloads.customers.keyword"
                    }
                },
                "stage_burn_time_avg": {
                    "avg": {
                        "field": "rocket.first_stage.burn_time_sec"
                    }
                },
                "launches_per_year": {
                    "date_histogram": {
                        "field": "date_utc",
                        "calendar_interval": "year"
                    }
                },
                "success_rate_by_rocket_type": {
                    "terms": {
                        "field": "rocket.name.keyword",
                        "size": 10
                    },
                "aggs": {
                    "success_count": {
                    "filter": {
                        "term": {
                        "success": True
                        }
                    }
                    },
                    "total_count": {
                    "value_count": {
                        "field": "rocket.name.keyword"
                    }
                    },
                    "success_rate": {
                    "bucket_script": {
                        "buckets_path": {
                        "successes": "success_count._count",
                        "total": "total_count"
                        },
                        "script": "params.successes / params.total"
                    }
                    }
                }
                },
                "cost_comparison_by_rocket_type": {
                    "terms": {
                        "field": "rocket.name.keyword",
                        "size": 10
                    },
                    "aggs": {
                        "average_cost": {
                        "avg": {
                            "field": "rocket.cost_per_launch"
                        }
                    }
                }
                }
            }
        }
        data = super().get_query(self.index, query)
        return from_dict(Dashboard, data)