import psycopg2
from connect import get_connection
from config import load_config
import csv

conn = get_connection()
cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            username VARCHAR(50) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """)
    conn.commit()

def insert_from_console():
    username = input("Username: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
        (username, phone)
    )
    conn.commit()
    print("Added")

def insert(username, phone):
    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT DO NOTHING",
        (username, phone)
    )
    conn.commit()
    print("Added")

def update_contact():
    username = input("who update: ")
    new_phone = input("New number: ")

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE username=%s",
        (new_phone, username)
    )
    conn.commit()
    print("Updateted")

def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_by_name():
    name = input("input name: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE username ILIKE %s",
        ('%' + name + '%',)
    )
    print(cur.fetchall())

def search_by_prefix():
    prefix = input("prefix: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + '%',)
    )
    print(cur.fetchall())

def delete_contact():
    choice = input("1-name, 2-phone: ")

    if choice == '1':
        username = input("Username: ")
        cur.execute("DELETE FROM phonebook WHERE username=%s", (username,))
    elif choice == '2':
        phone = input("Phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    print("delete")

def menu():
    while True:
        print("\n1.CSV")
        print("2.Console")
        print("3.Update")
        print("4.Show all")
        print("5.Search name")
        print("6.Search prefix")
        print("7.Delete")
        print("8.create table")
        print("0.Exit")

        ch = input("choose: ")

        if ch == '1':
            with open('cont.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    insert(username=row["username"],phone=row["phone"])
        elif ch == '2':
            insert_from_console()
        elif ch == '3':
            update_contact()
        elif ch == '4':
            show_all()
        elif ch == '5':
            search_by_name()
        elif ch == '6':
            search_by_prefix()
        elif ch == '7':
            delete_contact()
        elif ch == '8':
            create_table()
        elif ch == '0':
            break


menu()

cur.close()
conn.close()