#!/bin/bash
set -e

echo "🔧 Starting PostgreSQL entrypoint..."

# Start Postgres in the background
docker-entrypoint.sh postgres &

# Wait for postgres
until pg_isready -h localhost -U postgres; do
    echo "⏳ Waiting for PostgreSQL..."
    sleep 2
done

echo "✅ PostgreSQL is ready."

# Check if this is first-run (empty database)
COUNT=$(psql -U postgres -d sqldb -tAc "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='public';")

if [ "$COUNT" -eq "0" ]; then
    echo "🆕 Fresh database detected — running schema creation..."
    psql -U postgres -d sqldb -f /docker-entrypoint-initdb.d/01-create-tables.sql

    echo "🌱 Seeding initial CSV data..."
    python3 /postgres/seed.py
else
    echo "📦 Existing database detected — skipping auto-seed."
fi

wait