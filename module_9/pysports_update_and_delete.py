"""
    Title: pysports_update_and_delete.py
    Author: Chris Sewalson
    Date: Dec 4, 2021
    Description: Adding 
"""

""" import statements """
from dns.query import _set_selector_class
import mysql.connector
from mysql.connector import errorcode

""" database login """
config = {
    "user": "pysports_user",
    "password": "MySQLpassword1!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

# defining a method to call that will execute the inner join on the team and player tables
#   , iterate through the results and display it

def Show_players(cursor, title):
    # inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get results from cursor
    players = cursor.fetchall()

    print("\n == {} ==\n".format(title))

    # iterate through player data and display the reuslts
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
    
try:
    """ try and catch block for handling errors connecting to MySQL"""

    db = mysql.connector.connect(**config) # connecting to database

    # to start fresh, lines 46, 47 & 48 will
    #           delete all players not inserted from earlier assignments
    
    # cursor = db.cursor()
    # delete_player = ("DELETE FROM player WHERE player_id >= '7'")
    # cursor.execute(delete_player)
    
    cursor = db.cursor()
    
    # show the records before insert
    Show_players(cursor, "Displaying original records")

    cursor = db.cursor()

    # new player insert query
    add_player = ("INSERT INTO player(first_name, last_name, team_id)""VALUES(%s, %s, %s)")

    # new player data
    player_data = ("Smeagol", "Shire Folk", 1)

    # insert new player
    cursor.execute(add_player, player_data)

    # commit the insert
    db.commit()

    # show the records after insert
    Show_players(cursor, "Displaying records with new player")

    # update the new player
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    # execute the update
    cursor.execute(update_player)

    # show records
    Show_players(cursor, "Displaying results after player update")

    # delete the new player
    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    # execute the deletion
    cursor.execute(delete_player)

    # show all records after deletion
    Show_players(cursor, "Displaying players after new player was deleted")

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    """ error handling """
   
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username and/or password are incorrect")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database does not exist")

    else:
        print(err)

finally:
    db.close()
