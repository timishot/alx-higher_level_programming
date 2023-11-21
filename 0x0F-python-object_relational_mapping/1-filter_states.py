#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check for the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Capture command line arguments
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]
    host = "localhost"
    # Connect to the MySQL server
    db = MySQLdb.connect(host, port=3306,
                         user=username, passwd=password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE LEFT(name, 1)\
          = 'N' ORDER BY states.id ASC"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
