#!/usr/bin/python3
"""
Module that connects a python script to a database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # connect to the database using arguments from the cli
    my_db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    # create cursor object
    cur = my_db.cursor()

    # executing mysql queries
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # obtaining query result
    my_data = cur.fetall()

    # iterate through the data and print
    for row in my_data:
        print(row)

    # Close all cursors
    cur.close()

    # Close all databases
    my_db.close()
