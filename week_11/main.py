import psycopg2
from config import load_config

sql = """INSERT INTO book(name, phone)
             VALUES((%s), %s);"""


def add_update_user():
    new_name = input("Enter your name:")
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name FROM book WHERE name = %s", (new_name,))
                if cur.fetchone():
                    print("user already exist")
                    ch = input(
                        """Do you want update the number?
                        Yes <------> No
                        """
                    )
                    if ch == "Yes":
                        new_number = input("enter the number you want to change to:")
                        cur.execute(
                            "SELECT name FROM book WHERE name = %s", (new_name,)
                        )
                        if cur.fetchone():
                            cur.execute(
                                "UPDATE book SET phone = %s WHERE name = %s",
                                (new_number, new_name),
                            )
                            conn.commit()
                else:
                    new_number = int(input("enter number:"))
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
            cur.execute("SELECT * FROM book")
            rows = cur.fetchall()
            for row in rows:
                print(row)


def delete_user():
    change_user = input("Username: ")
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM book WHERE name = %s", (change_user,))
            if cur.fetchone():
                cur.execute("DELETE FROM book WHERE name = %s", (change_user,))
            else:
                print("error")

def add_users():
    userlist = list(map(str,input().split(" ")))
    numlist = list(map(int, input().split()))
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            for i in range(len(userlist)):
                cur.execute(sql, (userlist[i],numlist[i]))
            conn.commit()


"""def change_user_phone():
    change_user = input("Username: ")
    change_phone = input("enter the number you want to change to:")
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM book WHERE name = %s", (change_user,))
            if cur.fetchone():
                cur.execute(
                    "UPDATE book SET phone = %s WHERE name = %s",
                    (change_phone, change_user),
                )
            else:
                print("error")
"""

def find_user():
    finding = input("Username: ")
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM book")
            rows = cur.fetchall()
            for row in rows:
                if row[1] == finding:
                    print(f"user number: {row[2]}")


def show():
    print(
        """
           1 - add user
           2 - delete user
           3 - add users
           4 - list
           5 - search
           """
    )

    current_menu = int(input("menu:"))

    if 1 == current_menu:
        add_update_user()
    if 2 == current_menu:
        delete_user()
    if 3 == current_menu:
        add_users()
    if 4 == current_menu:
        list_of_members()
    if 5 == current_menu:
        find_user()

show()
