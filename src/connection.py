import MySQLdb

try:
    db = MySQLdb.connect (user='root', passwd='rahul3',
                         host='127.0.0.1',
                          db="srms")
    cursor = db.cursor ()
except:
    print("connection failed")