from typing import List, Optional
from app.domain.rockets import Rocket
import psycopg2
from psycopg2.extras import DictCursor
from app.ports.rockets import RocketRepository


class RocketRepository(RocketRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def create(self, name: str, description: str) -> Rocket:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "INSERT INTO rockets (name, description) VALUES (%s, %s) RETURNING id",
                    (name, description),
                )
                rocket_id = cur.fetchone()[0]
                return Rocket(id=rocket_id, name=name, description=description)

    def get(self, rocket_id: int) -> Optional[Rocket]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "SELECT id, name, description FROM rockets WHERE id = %s",
                    (rocket_id,),
                )
                result = cur.fetchone()
                if result:
                    return Rocket(
                        id=result["id"],
                        name=result["name"],
                        description=result["description"],
                    )
                return None

    def get_all(self) -> List[Rocket]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT id, name, description FROM rockets")
                results = cur.fetchall()
                return [
                    Rocket(
                        id=result["id"],
                        name=result["name"],
                        description=result["description"],
                    )
                    for result in results
                ]

    def update(self, rocket_id: int, name: str, description: str) -> Optional[Rocket]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "UPDATE rockets SET name = %s, description = %s WHERE id = %s RETURNING id",
                    (name, description, rocket_id),
                )
                if cur.rowcount > 0:
                    return Rocket(id=rocket_id, name=name, description=description)
                return None

    def delete(self, rocket_id: int) -> bool:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "DELETE FROM rockets WHERE id = %s RETURNING id",
                    (rocket_id,),
                )
                if cur.rowcount > 0:
                    return True
                return False
