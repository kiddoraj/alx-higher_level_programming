#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL connection parameters and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute a parameterized SQL query to retrieve cities of the specified state
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                       "INNER JOIN states ON cities.state_id = states.id "
                       "WHERE states.name = %s ORDER BY cities.id ASC", (state_name, ))

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        if db:
            db.close()
