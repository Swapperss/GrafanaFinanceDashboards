import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Loads values from .env


def get_db_connection():
    host = os.getenv("DB_HOST")
    port = 5432  # Default PostgreSQL port
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
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