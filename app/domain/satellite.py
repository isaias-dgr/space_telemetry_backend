from pydantic import BaseModel
from typing import Optional, List


class SpaceTrack(BaseModel):
    CCSDS_OMM_VERS: str
    COMMENT: str
    CREATION_DATE: str
    ORIGINATOR: str
    OBJECT_NAME: str
    OBJECT_ID: str
    CENTER_NAME: str
    REF_FRAME: str
    TIME_SYSTEM: str
    MEAN_ELEMENT_THEORY: str
    EPOCH: str
    MEAN_MOTION: float
    ECCENTRICITY: float
    INCLINATION: float
    RA_OF_ASC_NODE: float
    ARG_OF_PERICENTER: float
    MEAN_ANOMALY: float
    EPHEMERIS_TYPE: int
    CLASSIFICATION_TYPE: str
    NORAD_CAT_ID: int
    ELEMENT_SET_NO: int
    REV_AT_EPOCH: int
    BSTAR: float
    MEAN_MOTION_DOT: float
    MEAN_MOTION_DDOT: float
    SEMIMAJOR_AXIS: float
    PERIOD: float
    APOAPSIS: float
    PERIAPSIS: float
    OBJECT_TYPE: str
    RCS_SIZE: Optional[float | str] = None
    COUNTRY_CODE: Optional[str]
    LAUNCH_DATE: Optional[str]
    SITE: Optional[str]
    DECAY_DATE: Optional[str] = None
    DECAYED: int
    FILE: int
    GP_ID: int
    TLE_LINE0: str
    TLE_LINE1: str
    TLE_LINE2: str


class Satellite(BaseModel):
    spaceTrack: SpaceTrack
    version: Optional[str]
    launch: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    height_km: Optional[float]
    velocity_kms: Optional[float]
    id: str


Satellites = List[Satellite]
