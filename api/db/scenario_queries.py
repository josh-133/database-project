from db.connection import get_conn, release_conn

def get_scenarios():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    scenario_id,
                    scenario_name,
                    scenario_description,
                    predicted_weather,
                    start_time
                FROM scenario s
                ORDER BY s.scenario_id ASC;
            """)

            rows = cur.fetchall()

            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
    finally:
        release_conn(conn)
        
def create_scenario(data):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO scenario (
                    scenario_name,
                    scenario_description,
                    predicted_weather,
                    start_time
                )
                VALUES (%s, %s, %s, %s)
                RETURNING scenario_id;
            """, (
                data.scenario_name,
                data.scenario_description,
                data.predicted_weather,
                data.start_time
            ))

            new_id = cur.fetchone()[0]
            conn.commit()
            return new_id
    finally:
        release_conn(conn)
        
def update_scenario(scenario_id: int, data):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE  scenario
                SET
                    scenario_name = %s,
                    scenario_description = %s,
                    predicted_weather = %s,
                    start_time = %s
                WHERE scenario_id = %s
            """, (
                data.scenario_name,
                data.scenario_description,
                data.predicted_weather,
                data.start_time,
                data.scenario_id
            ))

            if cur.rowcount == 0:
                return False
    
            conn.commit()
            return True
            
    finally:
        release_conn(conn)

def delete_scenario(scenario_id: int):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM scenario
                WHERE scenario_id = %s
            """, (scenario_id,))

            if cur.rowcount == 0:
                return False
    
            conn.commit()
            return True
            
    finally:
        release_conn(conn)