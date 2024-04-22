import psycopg2
import csv
from config import load_config

sql = """INSERT INTO phonebook(name, phone)
             VALUES(%s, %s) RETURNING id;"""

def add_user():
    new_name, new_number = input("Enter your name:"), int(input("enter number:"))
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_name, new_number))
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def list_of_members():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            rows = cur.fetchall()
            for row in rows:
                print(row)

def delete_user():
    change_user = input("Username: ")
    config = load_config()
    with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                    cur.execute("SELECT name FROM phonebook WHERE name = %s", (change_user,))
                    if cur.fetchone():
                        cur.execute("DELETE FROM phonebook WHERE name = %s", (change_user,))
                    else:
                        print("error")

def change_user_phone():
    change_user = input("Username: ")
    change_phone =  (input("enter the number you want to change to:"))
    config = load_config()
    with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                    cur.execute("SELECT name FROM phonebook WHERE name = %s", (change_user,))
                    if cur.fetchone():
                        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (change_phone,change_user))
                    else:
                        print("error")

def find_user():
    finding = input("Username: ")
    config = load_config()
    with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebook")
                rows = cur.fetchall()
                for row in rows:
                    if row[1] == finding:
                        print(f"user number: {row[2]}")


def show():
    print(
        """
           1 - add user
           2 - delete user
           3 - change user
           4 - find user
           5 - list"""
    )

    current_menu = int(input("menu:"))

    if 1 == current_menu:
        add_user()
    if 2 == current_menu:
        delete_user()
    if 3 == current_menu:
        change_user_phone()
    if 4 == current_menu:
        find_user()
    if 5 == current_menu:
        list_of_members()


show()
