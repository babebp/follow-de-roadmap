import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE german_credit_risk (
            id INTEGER,
            Age INTEGER,
            Sex VARCHAR(20),
            Job INTEGER,
            Housing VARCHAR(20),
            "Saving accounts" VARCHAR(20),
            "Checking account" VARCHAR(20),
            "Credit amount" INTEGER,
            Duration INTEGER,
            Purpose VARCHAR(20)
        )
        """,
        )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()