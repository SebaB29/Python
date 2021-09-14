from contact_book import *
from os import system

def main() -> None:

    contacts = Contacts()
    sql_connect = contacts.get_sql_connect()
    cursor = contacts.get_cursor()
    get_out = False

    while not get_out:

        system('clear')

        print("Welcome to the Contact Book")
        print("1 Add Contact")
        print("2 View Contacts")
        print("3 Delete Contact")
        print("4 Edit Contact")
        print("5 Exit")

        option = input("Chose an option:  ")

        system("clear")

        if option == "1" :
            contacts.add_contact(cursor)
        elif option == "2" :
            contacts.view_contacts(cursor)
        elif option == "3" :
            contacts.view_contacts(cursor)
            contacts.delete_contact(cursor)
        elif option == "4" :
            contacts.view_contacts(cursor)
            contacts.edit_contact(cursor)
        elif option == "5":
            sql_connect.close()
            get_out = True
            continue

        sql_connect.commit()
        input("\nPress ENTER to continue")

main()