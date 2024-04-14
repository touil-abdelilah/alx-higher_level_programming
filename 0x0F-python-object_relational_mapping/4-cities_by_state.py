#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


def list_cities_by_state(username, password, database):
    """
    Function to list all cities from the database hbtn_0e_4_usa
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the query to select all cities with state names
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")

    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get MySQL username, password,
    # and database name from command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities_by_state(username, password, database)
