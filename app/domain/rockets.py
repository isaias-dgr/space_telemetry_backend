from pydantic import BaseModel
from typing import List, Optional


class Height(BaseModel):
    meters: Optional[float]
    feet: Optional[float]


class Diameter(BaseModel):
    meters: Optional[float]
    feet: Optional[float]


class Mass(BaseModel):
    kg: Optional[float]
    lb: Optional[float]


class Thrust(BaseModel):
    kN: Optional[float]
    lbf: Optional[float]


class FirstStage(BaseModel):
    reusable: Optional[bool]
    engines: Optional[int]
    fuel_amount_tons: Optional[float]
    burn_time_sec: Optional[float]
    thrust_sea_level: Optional[Thrust]
    thrust_vacuum: Optional[Thrust]


class CompositeFairing(BaseModel):
    height: Optional[Height]
    diameter: Optional[Diameter]


class Payloads(BaseModel):
    option_1: Optional[str]
    composite_fairing: Optional[CompositeFairing]


class SecondStage(BaseModel):
    reusable: Optional[bool]
    engines: Optional[int]
    fuel_amount_tons: Optional[float]
    burn_time_sec: Optional[float]
    thrust: Optional[Thrust]
    payloads: Optional[Payloads]


class ISP(BaseModel):
    sea_level: Optional[float]
    vacuum: Optional[float]


class Engine(BaseModel):
    number: Optional[int]
    type: Optional[str]
    version: Optional[str]
    layout: Optional[str]
    isp: Optional[ISP]
    engine_loss_max: Optional[float]
    propellant_1: Optional[str]
    propellant_2: Optional[str]
    thrust_sea_level: Optional[Thrust]
    thrust_vacuum: Optional[Thrust]
    thrust_to_weight: Optional[float]


class LandingLeg(BaseModel):
    number: Optional[int]
    material: Optional[str]


class Rocket(BaseModel):
    name: Optional[str]
    type: Optional[str]
    active: Optional[bool]
    stages: Optional[int]
    boosters: Optional[int]
    cost_per_launch: Optional[float]
    success_rate_pct: Optional[float]
    first_flight: Optional[str]
    country: Optional[str]
    company: Optional[str]
    height: Optional[Height]
    diameter: Optional[Diameter]
    mass: Optional[Mass]
    payload_weights: Optional[
        List[dict]
    ]  # Assuming payload_weights is a list of dictionaries
    first_stage: Optional[FirstStage]
    second_stage: Optional[SecondStage]
    engines: Optional[Engine]
    landing_legs: Optional[LandingLeg]
    flickr_images: Optional[List[str]]
    wikipedia: Optional[str]
    description: Optional[str]


Rockets = List[Rocket]
