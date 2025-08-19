import sqlite3
import psycopg2
from psycopg2.extras import execute_values
import os
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
import time


import sqlite3  # Built-in Python module
import psycopg2
from psycopg2.extras import execute_values


def copy_data(sqlite_db_path, postgres_db_config):
    # Connect to SQLite database
    sqlite_conn = sqlite3.connect(sqlite_db_path)
    sqlite_cur = sqlite_conn.cursor()

    # Connect to PostgreSQL database
    postgres_conn = psycopg2.connect(**postgres_db_config)
    postgres_cur = postgres_conn.cursor()

    # List of tables to transfer
    tables = [
        "auth_group",
        "auth_user_user_permissions",
        "auth_user",
        "auth_group_permissions",
        "django_session",
        "django_content_type",
        "django_migrations",
        "auth_user_groups",
        "django_admin_log",
        "users_profile",
        "auth_permission",
        "api_dps",
        "main_divorce",
        "sqlite_sequence",
    ]
    # Loop through each table to copy data
    for table_name in tables:
        # Fetch data from SQLite
        sqlite_cur.execute(f"SELECT * FROM {table_name}")
        data = sqlite_cur.fetchall()

        if not data:
            print(f"No data found in table {table_name}, skipping...")
            continue  # Skip empty tables

        # Get column names for the table
        columns = [desc[0] for desc in sqlite_cur.description]
        columns_str = ", ".join(columns)  # Create a comma-separated string of columns

        # Use execute_values to bulk insert data into PostgreSQL
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES %s"
        execute_values(postgres_cur, insert_query, data)
        print(f"INSERT INTO {table_name} ({columns_str}) VALUES {data}")
        # time.sleep(3)

        print(f"Done copying data for table {table_name}")

    # Commit changes and close connections
    postgres_conn.commit()
    postgres_cur.close()
    postgres_conn.close()
    sqlite_cur.close()
    sqlite_conn.close()


# Example usage
sqlite_db_path = "./db.sqlite3"  # Replace with the actual path
postgres_db_config = {
    "user": env("DATABASE_USER"),
    "password": env("DATABASE_PASSWORD"),
    "host": env("DATABASE_HOST"),
    "port": env("DATABASE_PORT"),
}


# import os

print(os.path.exists("./db.sqlite3"))

copy_data(sqlite_db_path, postgres_db_config)
