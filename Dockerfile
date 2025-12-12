FROM postgres:16

# Install Python + psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip gcc python3-dev libpq-dev

# Install psycopg2
RUN apt-get update && apt-get install -y python3-psycopg2

# Copy seed script
COPY ./postgres/seed.py /postgres/seed.py

WORKDIR /postgres