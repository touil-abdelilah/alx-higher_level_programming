#!/usr/bin/python3
"""
Script to display all values in the states table of hbtn_0e_0_usa
where name matches the provided argument (safe from SQL injection)
"""

import sys
import MySQLdb


def safe_filter_states_by_name(username, password, database, state_name):
    """
    Function to filter states by name and display matching results
    (safe from SQL injection)
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Construct the SQL query with a parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the state_name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get MySQL username, password, database name,
    # and state name from command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    safe_filter_states_by_name(username, password, database, state_name)
