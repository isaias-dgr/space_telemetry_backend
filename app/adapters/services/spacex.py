import hashlib
from typing import Generator, List
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
        self.__endpoint_launches = "v4/launches/query"
        self.__endpoint_rockets = "v4/rockets"
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
            print(f"Getting launches page {page} {limit}")
            launches, has_next_page = self.__get_launches(page, limit)
            yield from launches
            if not has_next_page:
                break
            page += 1

    def get_rockets(self) -> Rockets:
        url = f"{self.__base_url}/{self.__endpoint_rockets}"
        response = httpx.get(url)
        if response.status_code == 200:
            return [Rocket(**rocket) for rocket in response.json()]
        else:
            raise Exception(
                f"Failed to get rockets. Status code: {response.status_code}"
            )

    def __get_starlink(
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
                "populate": ["payloads", "rocket"],
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

    def get_starlink(self, page=1, limit=50) -> Generator[Launch, None, None]:
        while True:
            print(f"Getting sats page {page} {limit}")
            satellites, has_next_page = self.__get_starlink(page, limit)
            yield from satellites
            if not has_next_page:
                break
            page += 1
