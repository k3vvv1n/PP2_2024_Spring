import psycopg2
from configsn import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        ''' CREATE TABLE snakedb(
                    user_login VARCHAR(255) NOT NULL,
                    last_score INT,
                    last_level INT,
                    last_FPS INT,
                    snake_len INT,
                    wall_len INT,
                    record INT)
            ''')
    try:
        configsn = load_config()
        with psycopg2.connect(**configsn) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(commands)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()