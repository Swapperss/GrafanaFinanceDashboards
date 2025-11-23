import psycopg2
import os
def get_db_connection():
    host = "financepostgres.cclwcm2i0y08.us-east-1.rds.amazonaws.com"
    port = 5432  # Default PostgreSQL port
    dbname = "postgres"
    user = "postgres"
    password = "postgres"
    # Retrieve database connection info from environment variables
    # DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://postgres:postgres@postgres:5432/postgres')
    #DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'
    # Connect to PostgreSQL
    conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password)
    return conn