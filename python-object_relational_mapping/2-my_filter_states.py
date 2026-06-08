#!/usr/bin/python3
"""Ce script liste les valeurs de la table states qui correspondent à l'argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC;", (state_name_searched,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
