from db.connection import get_conn, release_conn

def get_drivers():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    d.driver_id,
                    d.driver_name,
                    d.employee_number,
                    d.employee_start_date
                FROM driver d
                ORDER BY d.driver_id ASC;
            """)

            rows = cur.fetchall()

            columns = [desc[0] for desc in cur.description]
            return [dict(zip(columns, row)) for row in rows]
    finally:
        release_conn(conn)
        
def create_driver(data):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO driver (
                    driver_name,
                    employee_number,
                    employee_start_date
                )
                VALUES (%s, %s, %s)
                RETURNING driver_id;
            """, (
                data.driver_name,
                data.employee_number,
                data.employee_start_date,
            ))

            new_id = cur.fetchone()[0]
            conn.commit()
            return new_id
    finally:
        release_conn(conn)
        
def update_driver(driver_id: int, data):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE  driver
                SET
                    driver_name = %s,
                    employee_number = %s,
                    employee_start_date = %s
                WHERE driver_id = %s
            """, (
                data.driver_name,
                data.employee_number,
                data.employee_start_date,
                data.driver_id,
            ))

            if cur.rowcount == 0:
                return False
    
            conn.commit()
            return True
            
    finally:
        release_conn(conn)

def delete_driver(driver_id: int):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                DELETE FROM driver
                WHERE driver_id = %s
            """, (driver_id,))

            if cur.rowcount == 0:
                return False
    
            conn.commit()
            return True
            
    finally:
        release_conn(conn)