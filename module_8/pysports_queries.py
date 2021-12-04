"""
    Title: pysports_queries.py
    Author: recreated by Chris Sewalson
    Date: Nov 26, 2021
    Description: Test program for joining the player and team tables
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
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database

    cursor = db.cursor()

    # selecting query method for finding teams
    cursor.execute("SELECT team_id, team_name, mascot from team")

    # get results of cursor query for teams
    teams = cursor.fetchall()

    print("\n  --Team Records--")
    print()

    # iterating over the team records and displaying results

    for team in teams:
        print(" Team ID: {}\n Team Name: {}\n Mascot: {}\n".format(team[0], team[1], team[2]))
    
    # selecting query method for finding players
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # get results of cursor query for players
    players = cursor.fetchall()

    print("\n --Player Records--")
    print()

    # iterating over the player records and returning results 
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))
    
    input("\n\n Press the enter key")

except mysql.connector.Error as err:
    """error handling"""
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The username or password are incorrect!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" No specified database!")
    else:
        print(err)
finally:
    """closing database connection"""
    db.close()
    
