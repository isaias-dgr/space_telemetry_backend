from pydantic import BaseModel, Field
from typing import List, Optional


class Failure(BaseModel):
    time: Optional[int]
    altitude: Optional[int]
    reason: Optional[str]


class Fairings(BaseModel):
    reused: Optional[bool] = None
    recovery_attempt: Optional[bool] = None
    recovered: Optional[bool] = None
    ships: Optional[List[str]] = None


class Core(BaseModel):
    core: Optional[str] = None
    flight: Optional[int] = None
    gridfins: Optional[bool] = None
    legs: Optional[bool] = None
    reused: Optional[bool] = None
    landing_attempt: Optional[bool] = None
    landing_success: Optional[bool] = None
    landing_type: Optional[str] = None
    landpad: Optional[str] = None


class Patch(BaseModel):
    small: Optional[str] = None
    large: Optional[str] = None


class Reddit(BaseModel):
    campaign: Optional[str] = None
    launch: Optional[str] = None
    media: Optional[str] = None
    recovery: Optional[str] = None


class Flickr(BaseModel):
    small: Optional[List[str]] = None
    original: Optional[List[str]] = None


class Links(BaseModel):
    patch: Optional[Patch] = None
    reddit: Optional[Reddit] = None
    flickr: Optional[Flickr] = None
    presskit: Optional[str] = None
    webcast: Optional[str] = None
    youtube_id: Optional[str] = None
    article: Optional[str] = None
    wikipedia: Optional[str] = None


class Launch(BaseModel):
    flight_number: int
    name: str
    date_utc: str
    date_unix: int
    date_local: str
    date_precision: str = Field(..., pattern="^(half|quarter|year|month|day|hour)$")
    static_fire_date_utc: Optional[str] = None
    static_fire_date_unix: Optional[int] = None
    tdb: bool = False
    net: bool = False
    window: Optional[int] = None
    rocket: Optional[str] = None
    success: Optional[bool] = None
    failures: Optional[List[Failure]] = None
    upcoming: bool
    details: Optional[str] = None
    fairings: Optional[Fairings] = None
    crew: Optional[List[str]] = None
    ships: Optional[List[str]] = None
    capsules: Optional[List[str]] = None
    payloads: Optional[List[str]] = None
    launchpad: Optional[str] = None
    cores: Optional[List[Core]] = None
    links: Optional[Links] = None
    auto_update: bool = True


Launches = List[Launch]
