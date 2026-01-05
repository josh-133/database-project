from db.connection import get_conn, release_conn

def get_driver_week_data():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    dwd.driver_week_id,
                    dwd.week_start_date,
                    dwd.mon_km, dwd.tue_km, dwd.wed_km,
                    dwd.thu_km, dwd.fri_km, dwd.sat_km, dwd.sun_km,
                    dwd.seatbelt_violations,

                    -- foreign key data
                    d.driver_id,
                    d.driver_name,

                    s.scenario_id,
                    s.scenario_name
                FROM driver_week_data dwd
                JOIN driver d ON dwd.driver_id = d.driver_id
                JOIN scenario s ON dwd.scenario_id = s.scenario_id
                ORDER BY dwd.week_start_date DESC;
            """)

            rows = cur.fetchall()

            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
    finally:
        release_conn(conn)
        
def create_driver_week_data(data):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO driver_week_data (
                    driver_id, scenario_id, week_start_date,
                    mon_km, tue_km, wed_km, thu_km,
                    fri_km, sat_km, sun_km,
                    seatbelt_violations
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING driver_week_id;
            """, (
                data.driver_id,
                data.scenario_id,
                data.week_start_date,
                data.mon_km,
                data.tue_km,
                data.wed_km,
                data.thu_km,
                data.fri_km,
                data.sat_km,
                data.sun_km,
                data.seatbelt_violations,
            ))

            new_id = cur.fetchone()[0]
            conn.commit()
            return new_id
    finally:
        release_conn(conn)
        
def update_driver_week_data(driver_week_id: int, data):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE  driver_week_data
                SET
                    week_start_date = %s,
                    mon_km = %s,
                    tue_km = %s,
                    wed_km = %s,
                    thu_km = %s,
                    fri_km = %s,
                    sat_km = %s,
                    sun_km = %s,
                    seatbelt_violations = %s,
                    driver_id = %s,
                    scenario_id = %s
                WHERE driver_week_id = %s
            """, (
                data.week_start_date,
                data.mon_km,
                data.tue_km,
                data.wed_km,
                data.thu_km,
                data.fri_km,
                data.sat_km,
                data.sun_km,
                data.seatbelt_violations,
                data.driver_id,
                data.scenario_id,
                data.driver_week_id,
            ))

            if cur.rowcount == 0:
                return False
    
            conn.commit()
            return True
            
    finally:
        release_conn(conn)

def delete_driver_week_data(driver_week_id: int):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM driver_week_data
                WHERE driver_week_id = %s
            """, (driver_week_id,))

            if cur.rowcount == 0:
                return False
    
            conn.commit()
            return True
            
    finally:
        release_conn(conn)