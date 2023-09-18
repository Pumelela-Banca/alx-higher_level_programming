#!/usr/bin/python3

"""
script that lists all states from the database
hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], database=sys.argv[3])
    with db.cursor() as cur:
        cur.excecute("SELECT * FROM states ORDER BY id")
        for i in cur.fetchall():
            print(i)
    db.close
