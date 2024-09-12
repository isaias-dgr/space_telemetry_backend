from dataclasses import asdict, dataclass, field
from typing import List, Optional

@dataclass
class Bucket:
    key: Optional[str] = None
    key_as_string: Optional[str] = None
    doc_count: int = 0
    total_count: Optional[dict] = field(default_factory=dict)
    success_count: Optional[dict] = field(default_factory=dict)
    success_rate: Optional[dict] = field(default_factory=dict)
    average_cost: Optional[dict] = field(default_factory=dict)

@dataclass
class Aggregation:
    doc_count_error_upper_bound: int = 0
    sum_other_doc_count: int = 0
    buckets: List[Bucket] = field(default_factory=list)

@dataclass
class AvgAggregation:
    value: float

@dataclass
class Dashboard:
    reusability_count: Aggregation
    engine_count_avg: AvgAggregation
    payload_weight_avg: AvgAggregation
    launch_success_rate: Aggregation
    success_rate_by_rocket_type: Aggregation
    launches_per_year: Aggregation
    stage_burn_time_avg: AvgAggregation
    cost_per_launch_avg: AvgAggregation
    average_thrust: AvgAggregation
    cost_comparison_by_rocket_type: Aggregation
    client_distribution: Aggregation
    launch_orbits: Aggregation

    def to_dict(self):
            return asdict(self)