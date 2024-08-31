from typing import List, Optional
from app.domain.launches import Launch
import psycopg2
from psycopg2.extras import DictCursor
from app.domain.launches import Launch
from app.ports.launches import LaunchRepository


class LaunchRepository(LaunchRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def create(self, name: str, description: str) -> Launch:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "INSERT INTO launches (name, description) VALUES (%s, %s) RETURNING id",
                    (name, description),
                )
                launch_id = cur.fetchone()[0]
                return Launch(id=launch_id, name=name, description=description)

    def get(self, launch_id: int) -> Optional[Launch]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "SELECT id, name, description FROM launches WHERE id = %s",
                    (launch_id,),
                )
                result = cur.fetchone()
                if result:
                    return Launch(
                        id=result["id"],
                        name=result["name"],
                        description=result["description"],
                    )
                return None

    def get_alls(self) -> List[Launch]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT id, name, description FROM launches")
                results = cur.fetchall()
                return [
                    Launch(
                        id=result["id"],
                        name=result["name"],
                        description=result["description"],
                    )
                    for result in results
                ]

    def update(self, launch_id: int, name: str, description: str) -> Optional[Launch]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "UPDATE launches SET name = %s, description = %s WHERE id = %s RETURNING id",
                    (name, description, launch_id),
                )
                if cur.rowcount > 0:
                    return Launch(id=launch_id, name=name, description=description)
                return None

    def delete(self, launch_id: int) -> bool:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    "DELETE FROM launches WHERE id = %s RETURNING id",
                    (launch_id,),
                )
                if cur.rowcount > 0:
                    return True
                return False
