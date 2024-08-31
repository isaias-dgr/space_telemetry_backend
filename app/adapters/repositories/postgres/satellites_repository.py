from typing import List, Optional
import psycopg2
from psycopg2.extras import DictCursor
from app.domain.satellite import Satellite
from app.ports.satellites import SatelliteRepository


class SatelliteRepository(SatelliteRepository):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def create(self, satellite: Satellite) -> Satellite:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    INSERT INTO satellites (
                        ccsds_omm_vers, comment, creation_date, originator, object_name,
                        object_id, center_name, ref_frame, time_system, mean_element_theory,
                        epoch, mean_motion, eccentricity, inclination, ra_of_asc_node,
                        arg_of_pericenter, mean_anomaly, ephemeris_type, classification_type,
                        norad_cat_id, element_set_no, rev_at_epoch, bstar, mean_motion_dot,
                        mean_motion_ddot, semimajor_axis, period, apoapsis, periapsis,
                        object_type, rcs_size, country_code, launch_date, site, decay_date,
                        decayed, file, gp_id, tle_line0, tle_line1, tle_line2
                    ) VALUES (
                        %(ccsds_omm_vers)s, %(comment)s, %(creation_date)s, %(originator)s, %(object_name)s,
                        %(object_id)s, %(center_name)s, %(ref_frame)s, %(time_system)s, %(mean_element_theory)s,
                        %(epoch)s, %(mean_motion)s, %(eccentricity)s, %(inclination)s, %(ra_of_asc_node)s,
                        %(arg_of_pericenter)s, %(mean_anomaly)s, %(ephemeris_type)s, %(classification_type)s,
                        %(norad_cat_id)s, %(element_set_no)s, %(rev_at_epoch)s, %(bstar)s, %(mean_motion_dot)s,
                        %(mean_motion_ddot)s, %(semimajor_axis)s, %(period)s, %(apoapsis)s, %(periapsis)s,
                        %(object_type)s, %(rcs_size)s, %(country_code)s, %(launch_date)s, %(site)s, %(decay_date)s,
                        %(decayed)s, %(file)s, %(gp_id)s, %(tle_line0)s, %(tle_line1)s, %(tle_line2)s
                    ) RETURNING id
                    """,
                    satellite.dict(),
                )
                satellite_id = cur.fetchone()[0]
                return Satellite(id=satellite_id, **satellite.dict())

    def get(self, satellite_id: int) -> Optional[Satellite]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    SELECT * FROM satellites WHERE id = %s
                    """,
                    (satellite_id,),
                )
                result = cur.fetchone()
                if result:
                    return Satellite(**result)
                return None

    def get_all(self) -> List[Satellite]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute("SELECT * FROM satellites")
                results = cur.fetchall()
                return [Satellite(**result) for result in results]

    def update(self, satellite_id: int, satellite: Satellite) -> Optional[Satellite]:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    UPDATE satellites SET
                        ccsds_omm_vers = %(ccsds_omm_vers)s, comment = %(comment)s,
                        creation_date = %(creation_date)s, originator = %(originator)s,
                        object_name = %(object_name)s, object_id = %(object_id)s,
                        center_name = %(center_name)s, ref_frame = %(ref_frame)s,
                        time_system = %(time_system)s, mean_element_theory = %(mean_element_theory)s,
                        epoch = %(epoch)s, mean_motion = %(mean_motion)s, eccentricity = %(eccentricity)s,
                        inclination = %(inclination)s, ra_of_asc_node = %(ra_of_asc_node)s,
                        arg_of_pericenter = %(arg_of_pericenter)s, mean_anomaly = %(mean_anomaly)s,
                        ephemeris_type = %(ephemeris_type)s, classification_type = %(classification_type)s,
                        norad_cat_id = %(norad_cat_id)s, element_set_no = %(element_set_no)s,
                        rev_at_epoch = %(rev_at_epoch)s, bstar = %(bstar)s, mean_motion_dot = %(mean_motion_dot)s,
                        mean_motion_ddot = %(mean_motion_ddot)s, semimajor_axis = %(semimajor_axis)s,
                        period = %(period)s, apoapsis = %(apoapsis)s, periapsis = %(periapsis)s,
                        object_type = %(object_type)s, rcs_size = %(rcs_size)s, country_code = %(country_code)s,
                        launch_date = %(launch_date)s, site = %(site)s, decay_date = %(decay_date)s,
                        decayed = %(decayed)s, file = %(file)s, gp_id = %(gp_id)s,
                        tle_line0 = %(tle_line0)s, tle_line1 = %(tle_line1)s, tle_line2 = %(tle_line2)s
                    WHERE id = %(satellite_id)s RETURNING id
                    """,
                    {"satellite_id": satellite_id, **satellite.dict()},
                )
                if cur.rowcount > 0:
                    return Satellite(id=satellite_id, **satellite.dict())
                return None

    def delete(self, satellite_id: int) -> bool:
        with psycopg2.connect(self.connection_string) as conn:
            with conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """
                    DELETE FROM satellites WHERE id = %s RETURNING id
                    """,
                    (satellite_id,),
                )
                if cur.rowcount > 0:
                    return True
                return False
