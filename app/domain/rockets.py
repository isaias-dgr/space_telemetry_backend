from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Height:
    meters: Optional[float] = None
    feet: Optional[float] = None


@dataclass
class Diameter:
    meters: Optional[float] = None
    feet: Optional[float] = None


@dataclass
class Mass:
    kg: Optional[float] = None
    lb: Optional[float] = None


@dataclass
class Thrust:
    kN: Optional[float] = None
    lbf: Optional[float] = None


@dataclass
class FirstStage:
    reusable: Optional[bool] = None
    engines: Optional[int] = None
    fuel_amount_tons: Optional[float] = None
    burn_time_sec: Optional[float] = None
    thrust_sea_level: Optional[Thrust] = None
    thrust_vacuum: Optional[Thrust] = None


@dataclass
class CompositeFairing:
    height: Optional[Height] = None
    diameter: Optional[Diameter] = None


@dataclass
class Payloads:
    option_1: Optional[str] = None
    composite_fairing: Optional[CompositeFairing] = None


@dataclass
class SecondStage:
    reusable: Optional[bool] = None
    engines: Optional[int] = None
    fuel_amount_tons: Optional[float] = None
    burn_time_sec: Optional[float] = None
    thrust: Optional[Thrust] = None
    payloads: Optional[Payloads] = None


@dataclass
class ISP:
    sea_level: Optional[float] = None
    vacuum: Optional[float] = None


@dataclass
class Engine:
    number: Optional[int] = None
    type: Optional[str] = None
    version: Optional[str] = None
    layout: Optional[str] = None
    isp: Optional[ISP] = None
    engine_loss_max: Optional[float] = None
    propellant_1: Optional[str] = None
    propellant_2: Optional[str] = None
    thrust_sea_level: Optional[Thrust] = None
    thrust_vacuum: Optional[Thrust] = None
    thrust_to_weight: Optional[float] = None


@dataclass
class LandingLeg:
    number: Optional[int] = None
    material: Optional[str] = None


@dataclass
class Rocket:
    name: Optional[str] = None
    type: Optional[str] = None
    active: Optional[bool] = None
    stages: Optional[int] = None
    boosters: Optional[int] = None
    cost_per_launch: Optional[float] = None
    success_rate_pct: Optional[float] = None
    first_flight: Optional[str] = None
    country: Optional[str] = None
    company: Optional[str] = None
    height: Optional[Height] = None
    diameter: Optional[Diameter] = None
    mass: Optional[Mass] = None
    payload_weights: Optional[List[dict]] = None
    first_stage: Optional[FirstStage] = None
    second_stage: Optional[SecondStage] = None
    engines: Optional[Engine] = None
    landing_legs: Optional[LandingLeg] = None
    flickr_images: Optional[List[str]] = None
    wikipedia: Optional[str] = None
    description: Optional[str] = None


Rockets = List[Rocket]
