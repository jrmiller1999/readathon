#!/usr/bin/python

import MySQLdb as mdb, sys

print "Content-type: text/html\n\n"

print "<h1>Welcome to the Northside Readathon for 2015-2016</h1>"

try: 
    con = mdb.connect ('localhost', 'nes_read', 'readingrocks', 'readathon2015')
    cursor = con.cursor()


except mdb.Error, e:
    print "Error in connection to %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

try: 
    query = "select count(*) from grades"
    cursor.execute(query)
    result = cursor.fetchone()
#    while (gradeline = result.fetch_row()

except mdb.Error as e:
    print "Error in query: %s" % query
    sys.exit(1)


print "there are %s grades at NES." % result

if con:
   con.close()


