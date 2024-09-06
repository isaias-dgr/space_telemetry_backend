from dataclasses import asdict, dataclass
from typing import List, Optional


@dataclass
class Patch:
    small: Optional[str]
    large: Optional[str]


@dataclass
class Reddit:
    campaign: Optional[str]
    launch: Optional[str]
    media: Optional[str]
    recovery: Optional[str]


@dataclass
class Flickr:
    small: List[str]
    original: List[str]


@dataclass
class Links:
    patch: Patch
    reddit: Reddit
    flickr: Flickr
    presskit: Optional[str]
    webcast: Optional[str]
    youtube_id: Optional[str]
    article: Optional[str]
    wikipedia: Optional[str]


@dataclass
class Fairings:
    reused: Optional[bool]
    recovery_attempt: Optional[bool]
    recovered: Optional[bool]
    ships: List[str]


@dataclass
class Core:
    core: Optional[str]
    flight: Optional[int]
    gridfins: Optional[bool]
    legs: Optional[bool]
    reused: Optional[bool]
    landing_attempt: Optional[bool]
    landing_success: Optional[bool]
    landing_type: Optional[str]
    landpad: Optional[str]


@dataclass
class Launch:
    fairings: Fairings
    links: Links
    static_fire_date_utc: Optional[str]
    static_fire_date_unix: Optional[int]
    net: bool
    window: Optional[int]
    rocket: str
    success: Optional[bool]
    failures: List[str]
    details: Optional[str]
    crew: List[str]
    ships: List[str]
    capsules: List[str]
    payloads: List[str]
    launchpad: str
    flight_number: int
    name: str
    date_utc: str
    date_unix: int
    date_local: str
    date_precision: str
    upcoming: bool
    cores: List[Core]
    auto_update: bool
    tbd: bool
    launch_library_id: Optional[str]
    id: str

    def to_dict(self):
        return asdict(self)


Launches = List[Launch]
