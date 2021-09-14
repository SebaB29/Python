from sqlite3 import *

class Contacts:

    def __init__(self: object) -> None:
        """..."""

        self.__sql_connect = connect("Contacts.db")
        self.__my_cursor = self.__sql_connect.cursor()
        try:
            self.__my_cursor.execute("CREATE TABLE Contacts (Id INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(20), Last Name VARCHAR(20), Tel VARCHAR(20))")
        except:
            pass
    
    def get_cursor(self: object):
        """..."""

        return self.__my_cursor

    def get_sql_connect(self: object):
        """..."""

        return self.__sql_connect

    def add_contact(self: object, cursor) -> None:
        """..."""

        print("Add Contact\n")
        name = input("Name:  ").capitalize()
        last_name = input("Last Name:  ").capitalize()
        telephone = input("Tel:  ")

        cursor.execute(f"INSERT INTO Contacts VALUES(NULL, '{name}', '{last_name}', '{telephone}')")

    def view_contacts(self: object, cursor):
        """..."""

        print("Contacts\n")

        print("+----+--------------------+--------------------+--------------------+")
        print("|ID  |Name                |Last Name           |Tel                 |")
        print("+----+--------------------+--------------------+--------------------+")

        cursor.execute("SELECT * FROM Contacts")

        contacts = cursor.fetchall()
        for contact in contacts:
            print(f"|{contact[0]:<4}|{contact[1]:<20}|{contact[2]:<20}|{contact[3]:<20}|")
            print("+----+--------------------+--------------------+--------------------+")

    def delete_contact(self: object, cursor) -> None:
        """..."""

        print("Delete Contact\n")
        contact_id = input("Enter contact ID:  ")

        cursor.execute(f"DELETE FROM Contacts WHERE Id = '{contact_id}'")

    def edit_contact(self: object, cursor) -> None:
        """..."""

        print("Edit Contact\n")
        contact_id = input("Enter contact ID:  ")
        new_telephone = input("Enter new tel:  ")

        cursor.execute(f"UPDATE Contacts SET Tel = '{new_telephone}' WHERE Id = '{contact_id}'")