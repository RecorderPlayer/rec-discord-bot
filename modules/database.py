from multiprocessing import connection
import psycopg2

cursor = None
conn = None

class Database:
    """Main Database Class"""

    def __init__(self, host: str, dbname: str, user: str, passwd: str):
        self.conn = psycopg2.connect(
            host=host,
            database=dbname,
            user=user,
            password=passwd
        )
        self.cursor = self.conn.cursor()

    def exec(self, query: str):
        try:
            responce = self.cursor.execute(query)
        except Exception as e:
            print(e)
    
    def write_user(self, wallet: str, insta: str, tg: int):
        try:
            self.cursor.execute(f"INSERT INTO users (insta_id, tg_id, insta_sub, tg_sub, wallet) VALUES ('{insta}', {tg}, false, false, '{wallet}')")
            self.conn.commit()
            return True
        except psycopg2.errors.UniqueViolation:
            return "alr"
        except Exception as e:
            print(e)
            return False

    def create_tables(self) -> None:
        """
        Creates tables (if not exist)
        """
        print("Preparing tables...")
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users(
                id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                insta_id CHAR(31) NOT NULL,
                tg_id INT NOT NULL,
                insta_sub BOOLEAN,
                tg_sub BOOLEAN,
                wallet CHAR(42) NOT NULL,
                CONSTRAINT insta_unique UNIQUE (insta_id),
                CONSTRAINT tg_unique UNIQUE (tg_id),
                CONSTRAINT wallet_unique UNIQUE (wallet)
            )
            """,
        )
        try:
            # create table one by one
            for command in commands:
                self.cursor.execute(command)
            # close communication with the PostgreSQL database server
            self.cursor.close()
            # commit the changes
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()