#!/usr/bin/python3

"""
script that lists all states from the database
hbtn_0e_0_usa filter using user input
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    safe = sys.argv[4]
    data = []
    with db.cursor() as cur:
        cur.execute("SELECT DISTINCT name FROM states")
        if safe not in cur.fetchall():
            exit()
        cur.execute("""SELECT * FROM states
         WHERE name LIKE BINARY '{}' ORDER BY id""".format(safe))
        for i in cur.fetchall():
            print(i)
    db.close
