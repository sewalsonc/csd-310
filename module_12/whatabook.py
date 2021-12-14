""" 
    WhatABook online bookstore SQL code
    Created by Chris Sewalson
    12/12/2021
    This code forms the user interface for the WhatABook online bookstore
"""

# import statements
import sys
import mysql.connector
from mysql.connector import errorcode

# whatabook database access information 
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_locations(_cursor):
    # selecting store location info to return
    _cursor.execute("SELECT store_id, locale from store")

    # returning cursor results as var locations
    locations = _cursor.fetchall()

    print("\n  -- What-A-Book Locations --")

    # iterate over the locations in store and displaying results(only 1 location thou)
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_user():
    # User ID verification method
    try:
        user_id = int(input('Enter customer id (user_id) here:'))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer id, enter the correct customer id number!\n")
            
            return validate_user
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  -- Invalid entry! -- \n")

        sys.exit(0)

def show_account_menu():
    # showing user account login options

    try:
        print("\n\t      -- What-A-Book Customer Account Menu --")
        print("To select an option below, type the number shown to the left of the desired option.\n1.\t Wishlist\n2.\t Add Book\n3.\t Main Menu")
        account_option = int(input('Enter the number here: '))

        return account_option
    except ValueError:
        print("\n  Invalid number!\n")

        # exiting account
        sys.exit(0)

def show_wishlist(_cursor, _user_id):
    
    # database query to pull users and wishlist books using inner joins to join user_id and book_id on wishlist table
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        -- Displaying wishlist table for What-A-Book customer --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def show_menu():
    print("\n  -- MAIN MENU --")

    print("To select an option below, type the number shown to the left of the selection.\n1.\t View Books\n2.\t View Store Locations\n3.\t My Account\n4.\t Exit Program")

    try:
        choice = int(input('Enter option here - Example: type 1 to View Books!>: '))

        return choice
    except ValueError:
        print("\n  Invalid entry!\n")
        
        return show_menu
        sys.exit(0)

def show_books(_cursor):
    # selecting book info to return - all book info selected 
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # gettin the results from the cursor and assigning to var books 
    books = _cursor.fetchall()

    print("\n  -- Books available at What-A-Book --")
    
    # iterate over books at WhatABook and display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

def show_books_to_add(_cursor, _user_id):
    
    #  query the database for available books for user
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_available = _cursor.fetchall()

    print("\n        -- The following books are available! --")

    for book in books_available:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # try/catch block for handling database errors  

    # connect to the What-A-Book database
    db = mysql.connector.connect(**config)  

    # cursor for MySQL queries
    cursor = db.cursor() 

    print("\n  Welcome to the WhatABook!  ")

    # show the main menu (call show_menu method)
    user_selection = show_menu()  

    # while loop if option 4(exit program) is not selected
    while user_selection != 4:

        # option 1 call the show_books method
        if user_selection == 1:
            show_books(cursor)

        # option 2 calls the show_locations method
        if user_selection == 2:
            show_locations(cursor)

        # option 3 calls the validate_user method and show_account_menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # option 1 calls the show_wishlist() method to show users wishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                # option 2 calls the show_books_to_add method to show available books
                if account_option == 2:

                    # show the books not saved in users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # book_id input selection
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # call add_book_to_wishlist to put selected book in users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit()  

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid Entry!  Please try again.")

                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid Entry!  Please try again")
            
        # return to main menu
        user_selection = show_menu()

    print("\n\n  Program Terminated!!")

except mysql.connector.Error as err:
    # handling errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  Username and/or password are incorrect!")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The database does not exist")

    else:
        print(err)

finally:
    # close the connection to MySQL

    db.close()