"""
    Title: pysports_join_queries.py
    Author: recreated by Chris Sewalson
    Date: Dec 4, 2021
    Description: Joining the player and team tables
"""

""" import statements """
from dns.query import _set_selector_class
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "MySQLpassword1!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try:
    """ try/catch block for handling potential errors"""

    db = mysql.connector.connect(**config) # this connects to mysql db

    cursor = db.cursor()

    # performing the inner join
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM play INNER JOIN team ON player.team_id = team.team_id")

    # initializing variable "players" with results of cursor.fetchall
    players = cursor.fetchall()

    print("\n --Player Records--")

    # iterating through player data and displaying results
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n Press any key to continue... ")

except mysql.connector.Error as err:
    """ error handling """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username and/or password are in correct")
    
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The database does not exist")
    
    else: 
        print(err)

finally:
    """ closing the sql connection """

    db.close()