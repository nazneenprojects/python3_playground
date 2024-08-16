"""

 database cursor is a mechanism that enables traversal over the records in a database.
  Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval, addition and removal of database records.
 The database cursor characteristic of traversal makes cursors akin to the programming language concept of iterator.


A database transaction symbolizes a unit of work, performed within a database management system (or similar system) against a database,
that is treated in a coherent and reliable way independent of other transactions.
A transaction generally represents any change in a database
"""


import sqlite3
con = sqlite3.connect("tutorial.db")                    # The returned Connection object con represents the connection to the on-disk database.
cur = con.cursor()                                      # To execute SQL statements and fetch results from SQL queries, need to use a database cursor.
cur.execute("CREATE TABLE movie(title, year, score)")   # execute a DDL query
res = cur.execute("SELECT name FROM sqlite_master")     # get the results
res.fetchone()                                          # get the results
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")       # get the results
res.fetchone() is None                                  # if non existent table  results is queried
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")                                                    # insert data
con.commit()                                            # commit tx