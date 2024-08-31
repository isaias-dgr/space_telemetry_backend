from typing import List
import httpx

from app.domain.launches import Launch, Launches
from app.domain.rockets import Rocket, Rockets
from app.domain.satellite import Satellite, Satellites


class SpaceXService:
    def __init__(
        self,
        base_url,
    ):
        self.__base_url = base_url
        self.__endpoint_launches = "v4/launches"
        self.__endpoint_rockets = "v4/rockets"
        self.__endpoint_starlinks = "v4/starlink"

    def get_launches(self) -> Launches:
        url = f"{self.__base_url}/{self.__endpoint_launches}"
        response = httpx.get(url)
        if response.status_code == 200:
            return [Launch(**launch) for launch in response.json()]
        else:
            raise Exception(
                f"Failed to get launches. Status code: {response.status_code}"
            )

    def get_rockets(self) -> Rockets:
        url = f"{self.__base_url}/{self.__endpoint_rockets}"
        response = httpx.get(url)
        if response.status_code == 200:
            return [Rocket(**rocket) for rocket in response.json()]
        else:
            raise Exception(
                f"Failed to get rockets. Status code: {response.status_code}"
            )

    def get_starlink(self) -> Satellites:
        url = f"{self.__base_url}/{self.__endpoint_starlinks}"
        print(url)
        response = httpx.get(url)
        if response.status_code == 200:
            return [Satellite(**sat) for sat in response.json()]
        else:
            raise Exception(
                f"Failed to get satellite. Status code: {response.status_code}"
            )
