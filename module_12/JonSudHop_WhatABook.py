#Jon Sudhop
#12-08-21
#What A Book - Development

#I tried to handle everything i could with the modules just passing the data around as needed. 
#As far as I recall the only reused code was from myself, though I can't be certain that when I used that code originally it wasn't something I had to look up.

#reused all of the stuff related to connecting from earlier assignments
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

try:
    #Connect to database
    db = mysql.connector.connect(**config)

    #cursor objects
    cursor = db.cursor()

    
#Error handling for connection
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The supplied username or password was invalid.')
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The specified database does not exist.')

    else:
        print(err)

finally:
    db.close


def validate_user():
    test = True
    while test:
        try:
            print('\n****************************************************************')

            uId = int(input('Please Enter Your User ID: '))
            cursor.execute('SELECT user_id From user')
            result = cursor.fetchall()
            
            #It didn't work at first, so I used the below line to check what was returning, I saw it was a tuple and then just compared that
            #print(result)
            
            if (uId, ) in result:
                print('User accepted.')
                test = False
                return uId
            else:
                print('Invalid input.  Please try again.')
                    
        except ValueError:
            print('Invalid input.  Please try again.')



def show_books():
    print('\n****************************************************************')
    print('Master list of all books-')
    print('')
    cursor.execute('SELECT book_name, author, book_id, details FROM book')
    books = cursor.fetchall()
    for book in books:
        print('Title: {}'.format(book[0]))
        print('Author: {}'.format(book[1]))
        print('ID number: {}'.format(book[2]))
        print('Description of title: {}'.format(book[3]))
        print('')
    print('\n****************************************************************')
    show_menu()

def show_locations():
    print('\n****************************************************************')
    print('Master list of all current What A Book Locations-')
    print('')
    cursor.execute('SELECT store_id, locale FROM store')
    stores = cursor.fetchall()
    for store in stores:
        print('Store Name: What A Book')
        print('Address: {}'.format(store[1]))
        print('Store number: {}'.format(store[0]))
    print('\n****************************************************************')
    show_menu()

def show_wishlist(uId):
    print('\n****************************************************************')
    print('Users wishlist contains: ')
    cursor.execute('SELECT book.book_id, book.book_name, book.author, user.user_id FROM wishlist INNER JOIN book ON wishlist.book_id = book.book_id INNER JOIN user ON wishlist.user_id = user.user_id WHERE wishlist.user_id = {}'.format(uId))
    wishes = cursor.fetchall()
    for wishlist in wishes:
        print('Book ID {} - {} by {}.'.format(wishlist[0], wishlist[1], wishlist[2]))
    print('\n****************************************************************')
    show_account_menu(uId)

def show_books_to_add(uId):
    print('\n****************************************************************')
    print('Please select from the following books to add: ')
    cursor.execute('SELECT book_id, book_name, author FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})'.format(uId))
    adds = cursor.fetchall()
    for add in adds:
        print('Book ID: {}'.format(add[0]))
        print('Book Name: {}'.format(add[1]))
        print('Book Author: {}'.format(add[2]))
        print('')
    print('\n****************************************************************')
    bId = int(input('Please select a book to add to your list, using it\'s Book ID number: '))
    return bId

def add_book_to_wishlist(uId, bId):
    print('\n****************************************************************')
    cursor.execute('INSERT INTO wishlist (user_id, book_id) Values ({}, {})'.format(uId, bId))
    show_account_menu(uId)

#This is the inner account manipulation loop 
def show_account_menu(uId):
    print('\n****************************************************************')
    cursor.execute('SELECT first_name, last_name FROM user WHERE user_id = {}'.format(uId))
    users = cursor.fetchall()
    for user in users:
        print('Welcome {} {}, please select from the following options.'.format(user[0], user[1]))
        print('\n[1] View Wishlist.')
        print('[2] Add a book to Wishlist.')
        print('[3] Return to Main Menu.')

        try: 
            selection = int(input())
            while selection:
                if selection == 1:
                    show_wishlist(uId)
                elif selection == 2:
                    add_book_to_wishlist(uId, show_books_to_add(uId))
                elif selection == 3:
                    show_menu() 
                else:
                    print('Invalid selection, please try again.')
                    show_account_menu(uId)
        except ValueError:
            print('Invalid selection, please try again.')
            show_account_menu(uId)

#This is the outer loop - it contains the main menu and controls initial flow
def show_menu():
    print('\n****************************************************************')
    print('\n          ****************MAIN MENU****************')
    print('          Please select from the following options: ')
    print('\n[1] View Books.')
    print('[2] View Store Locations.')
    print('[3] My Account.')
    print('[4] Exit the program.')
    print('\n****************************************************************')

#I use a try/except block to ensure proper input
    try: 
        selection = int(input())
        while selection:
            if selection == 1:
                show_books()
            elif selection == 2:
                show_locations()
            elif selection == 3:
                show_account_menu(validate_user())
            elif selection == 4:
                exit()
            else:
                print('Invalid selection, please try again.')
                show_menu()
    except ValueError:
        print('Invalid selection, please try again.')
        show_menu()

#This starts everything
print('\n****************************************************************')
print('Welcome to What A Book\'s New Inventory and Wishlisting Program!')
show_menu()