import psycopg2
import csv
from config import load_config

def insert_phonebook():
    """ Insert new entries from a CSV file into the phonebook table """

    sql = """INSERT INTO book(name, phone)
             VALUES(%s, %s);"""
    
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open('data.csv', 'r') as file:
                    reader = csv.reader(file)
                    for item in reader:
                        cur.execute(sql, (item[0], item[1]))

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    

if __name__ == '__main__':
    insert_phonebook()

