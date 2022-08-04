import psycopg2

def connect(host: str, dbname: str, user: str, passwd: str):
    """
    Connect to the database
    """
    print("- Connecting to database...")
    conn = psycopg2.connect(
        host=host,
        database=dbname,
        user=user,
        password=passwd
    )
    return conn

def create_tables(cursor, connection) -> None:
    """
    Creates tables (if not exist)
    """
    print("Preparing tables...")
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY,
            insta_id INT,
            tg_id INT,
            insta_sub CHAR,
            tg_sub CHAR,
            wallet CHAR NOT NULL
        )
        """,
    )
    try:
        # create table one by one
        for command in commands:
            cursor.execute(command)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


