from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class SpaceTrack:
    CCSDS_OMM_VERS: str = ""
    COMMENT: str = ""
    CREATION_DATE: str = ""
    ORIGINATOR: str = ""
    OBJECT_NAME: str = ""
    OBJECT_ID: str = ""
    CENTER_NAME: str = ""
    REF_FRAME: str = ""
    TIME_SYSTEM: str = ""
    MEAN_ELEMENT_THEORY: str = ""
    EPOCH: str = ""
    MEAN_MOTION: float = 0.0
    ECCENTRICITY: float = 0.0
    INCLINATION: float = 0.0
    RA_OF_ASC_NODE: float = 0.0
    ARG_OF_PERICENTER: float = 0.0
    MEAN_ANOMALY: float = 0.0
    EPHEMERIS_TYPE: int = 0
    CLASSIFICATION_TYPE: str = ""
    NORAD_CAT_ID: int = 0
    ELEMENT_SET_NO: int = 0
    REV_AT_EPOCH: int = 0
    BSTAR: float = 0.0
    MEAN_MOTION_DOT: float = 0.0
    MEAN_MOTION_DDOT: float = 0.0
    SEMIMAJOR_AXIS: float = 0.0
    PERIOD: float = 0.0
    APOAPSIS: float = 0.0
    PERIAPSIS: float = 0.0
    OBJECT_TYPE: str = ""
    RCS_SIZE: Optional[float | str] = None
    COUNTRY_CODE: Optional[str] = None
    LAUNCH_DATE: Optional[str] = None
    SITE: Optional[str] = None
    DECAY_DATE: Optional[str] = None
    DECAYED: int = 0
    FILE: int = 0
    GP_ID: int = 0
    TLE_LINE0: str = ""
    TLE_LINE1: str = ""
    TLE_LINE2: str = ""


@dataclass
class Satellite:
    spaceTrack: SpaceTrack
    version: Optional[str] = None
    launch: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    height_km: Optional[float] = None
    velocity_kms: Optional[float] = None
    id: str = ""

    def to_dict(self):
        return asdict(self)


Satellites = List[Satellite]


def to_dict(satellites: Satellites):
    return [satellite.to_dict() for satellite in satellites]
