import hashlib
from typing import Generator, List
import httpx

from app.domain.launches import Launch, Launches
from app.domain.rockets import Rocket, Rockets, from_dict
from app.domain.satellite import Satellite, Satellites


class SpaceXService:
    def __init__(
        self,
        base_url,
    ):
        self.__base_url = base_url
        self.__endpoint_launches = "v4/launches/query"
        self.__endpoint_rockets = "v4/rockets/query"
        self.__endpoint_starlinks = "v4/starlink/query"

    def __get_launches(
        self,
        page=1,
        limit=10,
    ):
        url = f"{self.__base_url}/{self.__endpoint_launches}"
        query = {
            "query": {},
            "options": {
                "page": page,
                "limit": limit,
                "populate": ["payloads", "rocket"],
            },
        }
        response = httpx.post(
            url, json=query, headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            return [Launch(**launch) for launch in data["docs"]], data["hasNextPage"]
        else:
            raise Exception(
                f"Failed to get launches. Status code: {response.status_code}"
            )

    def get_launches(self, page=1, limit=50) -> Generator[Launch, None, None]:
        while True:
            launches, has_next_page = self.__get_launches(page, limit)
            yield from launches
            if not has_next_page:
                break
            page += 1

    def __get_satellites(
        self,
        page=1,
        limit=10,
    ) -> Satellites:
        url = f"{self.__base_url}/{self.__endpoint_starlinks}"
        query = {
            "query": {},
            "options": {
                "page": page,
                "limit": limit,
            },
        }
        response = httpx.post(
            url, json=query, headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            return [Satellite(**sat) for sat in data["docs"]], data["hasNextPage"]
        else:
            raise Exception(
                f"Failed to get satellite. Status code: {response.status_code}"
            )

    def get_satellites(self, page=1, limit=50) -> Generator[Satellite, None, None]:
        while True:
            satellites, has_next_page = self.__get_satellites(page, limit)
            yield satellites
            if not has_next_page:
                break
            page += 1

    def __get_rockets(self, page=1, limit=50) -> Rockets:
        url = f"{self.__base_url}/{self.__endpoint_rockets}"
        query = {
            "query": {},
            "options": {"page": page, "limit": limit},
        }
        response = httpx.post(
            url, json=query, headers={"Content-Type": "application/json"}
        )
        if response.status_code == 200:
            data = response.json()
            return [from_dict(Rocket, r) for r in data["docs"]], data["hasNextPage"]
        else:
            raise Exception(
                f"Failed to get rockets. Status code: {response.status_code}"
            )

    def get_rockets(self, page=1, limit=50) -> Generator[Satellite, None, None]:
        while True:
            rockets, has_next_page = self.__get_rockets(page, limit)
            yield from rockets
            if not has_next_page:
                break
            page += 1
