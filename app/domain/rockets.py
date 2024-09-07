from dataclasses import dataclass, asdict
from decimal import Decimal
from typing import List, Optional


@dataclass
class Dimension:
    meters: Optional[Decimal]
    feet: Optional[Decimal]


@dataclass
class Mass:
    kg: Optional[Decimal]
    lb: Optional[Decimal]


@dataclass
class Thrust:
    kN: Optional[Decimal]
    lbf: Optional[Decimal]

@dataclass
class FirstStage:
    thrust_sea_level: Thrust
    thrust_vacuum: Thrust
    reusable: Optional[bool]
    engines: Optional[int]
    fuel_amount_tons: Optional[Decimal]
    burn_time_sec: Optional[int]

@dataclass
class CompositeFairing:
    height: Dimension
    diameter: Dimension

@dataclass
class Payloads:
    composite_fairing: CompositeFairing
    option_1: Optional[str]

@dataclass
class SecondStage:
    thrust: Thrust
    payloads: Payloads
    reusable: Optional[bool]
    engines: Optional[int]
    fuel_amount_tons: Optional[Decimal]
    burn_time_sec: Optional[int]


@dataclass
class ISP:
    sea_level: Optional[int]
    vacuum: Optional[int]


@dataclass
class Engines:
    isp: ISP
    thrust_sea_level: Thrust
    thrust_vacuum: Thrust
    number: Optional[int]
    type: Optional[str]
    version: Optional[str]
    layout: Optional[str]
    engine_loss_max: Optional[int]
    propellant_1: Optional[str]
    propellant_2: Optional[str]
    thrust_to_weight: Optional[Decimal]


@dataclass
class LandingLegs:
    number: Optional[int]
    material: Optional[str]


@dataclass
class PayloadWeight:
    id: Optional[str]
    name: Optional[str]
    kg: Optional[int]
    lb: Optional[int]


@dataclass
class Rocket:
    height: Dimension
    diameter: Dimension
    mass: Mass
    first_stage: FirstStage
    second_stage: SecondStage
    engines: Engines
    landing_legs: LandingLegs
    payload_weights: List[PayloadWeight]
    flickr_images: List[str]
    name: Optional[str]
    type: Optional[str]
    active: Optional[bool]
    stages: Optional[int]
    boosters: Optional[int]
    cost_per_launch: Optional[Decimal]
    success_rate_pct: Optional[Decimal]
    first_flight: Optional[str]
    country: Optional[str]
    company: Optional[str]
    wikipedia: Optional[str]
    description: Optional[str]
    id: Optional[str]

    def to_dict(self):
        return asdict(self)

Rockets = List[Rocket]
