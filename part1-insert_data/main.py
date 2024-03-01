import psycopg2

if __name__ == '__main__':

    # Connect postgresql database
    with psycopg2.connect(
        host="localhost",
        database="follow-de-roadmap",
        user="postgres",
        password="1234"
    ) as conn:
        print(conn.status)