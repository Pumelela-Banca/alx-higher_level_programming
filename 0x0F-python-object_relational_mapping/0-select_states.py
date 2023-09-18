#!/usr/bin/python3

"""
script that lists all states from the database
hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[2], port=3306,
                         passwd=sys.argv[3], db=sys.argv[4])
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id")
        for i in cur.fetchall():
            print(i)
    db.close
