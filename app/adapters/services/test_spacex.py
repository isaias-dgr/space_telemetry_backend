import pytest
from httpx import Response
from app.adapters.services.spacex import SpaceXService
from app.domain.launches import Launch
from app.domain.rockets import Rocket
from app.domain.satellite import Satellite


def test_get_launches():
    service = SpaceXService("https://api.spacexdata.com")
    result = service.get_launches()
    assert isinstance(result, list)
    assert isinstance(result[0], Launch)


def test_get_rockets():
    service = SpaceXService("https://api.spacexdata.com")
    result = service.get_rockets()
    assert isinstance(result, list)
    assert isinstance(result[0], Rocket)


def test_get_satellites():
    service = SpaceXService("https://api.spacexdata.com")
    result = service.get_satellites()
    assert isinstance(result, list)
    assert isinstance(result[0], Satellite)
