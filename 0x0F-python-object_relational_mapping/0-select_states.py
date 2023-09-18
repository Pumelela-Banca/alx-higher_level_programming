#!/usr/bin/python3

"""
script that lists all states from the database
hbtn_0e_0_usa
"""

import sys
from MySQLdb import _mysql


if __name__ == "__main__":
    db = _mysql.connect(host="localhost", user=sys.argv[1], port=3306,
                         password=sys.argv[2], database=sys.argv[3])
    try:
        db.query("SELECT * FROM states ORDER BY id")
        r = db.store_result()
        for i in r:
            print(i)
    except _mysql.MySQLError:
        pass
    db.close
