#!/usr/bin/python3

"""
lists all cities of a state
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])

    with db.cursor() as cur:
        cur.execute("""SELECT cities.id, cities.name,
         states.name FROM cities
         JOIN states ON cities.state_id = states.id
         ORDER BY cities.id""")
        for i in cur.fetchall():
            print(i)
    db.close()
