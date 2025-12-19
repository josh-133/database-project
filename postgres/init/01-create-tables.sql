CREATE TABLE driver (
    driver_id SERIAL PRIMARY KEY,
    driver_name VARCHAR(100) NOT NULL,
    employee_number VARCHAR(100) UNIQUE NOT NULL,
    employee_start_date DATE NOT NULL
);

CREATE TABLE scenario (
    scenario_id SERIAL PRIMARY KEY,
    scenario_name VARCHAR(100) NOT NULL,
    scenario_description VARCHAR(1000),
    predicted_weather VARCHAR(100),
    start_time TIMESTAMP NOT NULL
);

CREATE TABLE driver_week_data (
    driver_week_id SERIAL PRIMARY KEY,
    driver_id INTEGER NOT NULL REFERENCES driver(driver_id) ON DELETE CASCADE,
    scenario_id INTEGER NOT NULL REFERENCES scenario(scenario_id) ON DELETE CASCADE,
    week_start_date DATE NOT NULL,
    mon_km NUMERIC(6,2) NOT NULL,
    tue_km NUMERIC(6,2) NOT NULL,
    wed_km NUMERIC(6,2) NOT NULL,
    thu_km NUMERIC(6,2) NOT NULL,
    fri_km NUMERIC(6,2) NOT NULL,
    sat_km NUMERIC(6,2) NOT NULL,
    sun_km NUMERIC(6,2) NOT NULL,
    seatbelt_violations INTEGER NOT NULL
);

CREATE TABLE brand (
    brand_id SERIAL PRIMARY KEY,
    brand_name VARCHAR(100) NOT NULL
);

CREATE TABLE capability (
    capability_id SERIAL PRIMARY KEY,
    capability_name VARCHAR(100) NOT NULL
);

CREATE TABLE vulnerability (
    vulnerability_id SERIAL PRIMARY KEY,
    vulnerability_name VARCHAR(100) NOT NULL
);

CREATE TABLE vehicle (
    vehicle_id SERIAL PRIMARY KEY,
    vehicle_name VARCHAR(100) NOT NULL,
    brand_id INTEGER NOT NULL REFERENCES brand(brand_id) ON DELETE CASCADE,
    height DOUBLE PRECISION NOT NULL,
    max_speed INTEGER NOT NULL
);

CREATE TABLE vehicle_instance (
    vehicle_instance_id SERIAL PRIMARY KEY,
    rego VARCHAR(100) NOT NULL UNIQUE,
    scenario_id INTEGER NOT NULL REFERENCES scenario(scenario_id) ON DELETE CASCADE,
    vehicle_id INTEGER NOT NULL REFERENCES vehicle(vehicle_id) ON DELETE CASCADE,
    driver_id INTEGER NOT NULL REFERENCES driver(driver_id) ON DELETE CASCADE,
    UNIQUE(driver_id, scenario_id)
);

CREATE TABLE vehicle_capability (
    vehicle_id INTEGER NOT NULL REFERENCES vehicle(vehicle_id) ON DELETE CASCADE,
    capability_id INTEGER NOT NULL REFERENCES capability(capability_id) ON DELETE CASCADE,
    PRIMARY KEY (vehicle_id, capability_id)
);

CREATE TABLE vehicle_vulnerability (
    vehicle_id INTEGER NOT NULL REFERENCES vehicle(vehicle_id) ON DELETE CASCADE,
    vulnerability_id INTEGER NOT NULL REFERENCES vulnerability(vulnerability_id) ON DELETE CASCADE,
    PRIMARY KEY (vehicle_id, vulnerability_id)
);