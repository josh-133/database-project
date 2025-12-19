import csv
import psycopg2
from datetime import datetime

def parse_time(value: str) -> str:
    # value like "8pm"
    dt = datetime.strptime(value.strip().lower(), "%I%p")
    # return timestamp with default date
    return dt.replace(year=2025, month=1, day=1)

conn = psycopg2.connect(
    host="postgres",
    database="sqldb",
    user="postgres",
    password="password"
)
cursor = conn.cursor()

print("🌱 Seeding scenarios.csv...")

with open("/postgres/csvs/scenarios.csv") as f:
    reader = csv.DictReader(f)
    print("CSV headers:", reader.fieldnames) 
    for row in reader:
        parsed_time = parse_time(row["start_time"])
        
        cursor.execute("""
            INSERT INTO scenario (scenario_id, scenario_name, scenario_description, predicted_weather, start_time)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, (
            row["scenario_id"], 
            row["scenario_name"], 
            row["scenario_description"], 
            row["predicted_weather"],
            parsed_time,
        ))

print("🌱 Seeding drivers.csv...")

with open("/postgres/csvs/drivers.csv") as f:
    reader = csv.DictReader(f)
    print("CSV headers:", reader.fieldnames) 
    for row in reader:
        cursor.execute("""
            INSERT INTO driver (driver_id, driver_name, employee_number, employee_start_date)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, (
            row["driver_id"], 
            row["driver_name"], 
            row["employee_number"], 
            row["employee_start_date"]
        ))

print("🌱 Seeding brands.csv...")

with open("/postgres/csvs/brands.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
    INSERT INTO brand
        (brand_id, brand_name)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["brand_id"],
        row["brand_name"]
    ))
        
print("🌱 Seeding capabilities.csv...")

with open("/postgres/csvs/capabilities.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
    INSERT INTO capability
        (capability_id, capability_name)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["capability_id"],
        row["capability_name"]
    ))
        
print("🌱 Seeding vulnerabilities.csv...")

with open("/postgres/csvs/vulnerabilities.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
    INSERT INTO vulnerability
        (vulnerability_id, vulnerability_name)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["vulnerability_id"],
        row["vulnerability_name"]
    ))
        
print("🌱 Seeding vehicles.csv...")
        

with open("/postgres/csvs/vehicles.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
    INSERT INTO vehicle
        (vehicle_id, vehicle_name, brand_id, height, max_speed)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["vehicle_id"],
        row["vehicle_name"], 
        row["brand_id"], 
        row["height"], 
        row["max_speed"]
    ))
        
print("🌱 Seeding vehicle_vulnerabilities.csv...")

with open("/postgres/csvs/vehicle_vulnerabilities.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
    INSERT INTO vehicle_vulnerability
        (vehicle_id, vulnerability_id)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["vehicle_id"],
        row["vulnerability_id"]
    ))
        
print("🌱 Seeding vehicle_capabilities.csv...")

with open("/postgres/csvs/vehicle_capabilities.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
    INSERT INTO vehicle_capability
        (vehicle_id, capability_id)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["vehicle_id"],
        row["capability_id"]
    ))
        
with open("/postgres/csvs/vehicle_instances.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
    INSERT INTO vehicle_instance
        (vehicle_instance_id, rego, scenario_id, vehicle_id, driver_id)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["vehicle_instance_id"],
        row["rego"],
        row["scenario_id"],
        row["vehicle_id"],
        row["driver_id"]
    ))
        
print("🌱 Seeding driver_week_data.csv...")
        
with open("/postgres/csvs/driver_week_data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        week_start_date = datetime.strptime(
            row["week_start_date"],
            "%d/%m/%Y"
        ).date(),
        cursor.execute("""
    INSERT INTO driver_week_data
        (driver_id, scenario_id, week_start_date, mon_km, tue_km, wed_km, thu_km, fri_km, sat_km, sun_km, seatbelt_violations)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
    """, (
        row["driver_id"], 
        row["scenario_id"],
        week_start_date,
        row["mon_km"], 
        row["tue_km"], 
        row["wed_km"], 
        row["thu_km"], 
        row["fri_km"], 
        row["sat_km"], 
        row["sun_km"], 
        row["seatbelt_violations"]
    ))

conn.commit()
conn.close()

print("✅ Done seeding CSVs.")