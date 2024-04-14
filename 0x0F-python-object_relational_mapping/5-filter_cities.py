#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


def filter_cities_by_state(username, password, database, state_name):
    """
    Function to list all cities of a given state
    from the database hbtn_0e_4_usa
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the query to select all cities of the given state
    query = ("SELECT GROUP_CONCAT(name SEPARATOR ', ') "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Print the result
    if result:
        print(result)
    else:
        print("")

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get MySQL username, password,
    # database name, and state name from command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities_by_state(username, password, database, state_name)
