#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database with the provided credentials and database name
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()  # Create a cursor for executing SQL queries

    match = sys.argv[4]  # Get the state name to search for from the command line

    # Execute a parameterized SQL query to retrieve states that match the provided name
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    rows = cur.fetchall()  # Fetch all the rows that match the query

    # Print the retrieved rows, which represent the states that match the provided name
    for row in rows:
        print(row)

    cur.close()  # Close the cursor
    db.close()   # Close the database connection
