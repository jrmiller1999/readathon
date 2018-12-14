#!/usr/bin/python

import MySQLdb as mdb, sys
import jrm_db

print "Content-type: text/html\n\n"

print "<h1>Welcome to the Northside Readathon for 2015-2016</h1>"

connection = jrm_db.connect()
cursor = connection.cursor()

try: 
    query = "select count(*) from grades"
    cursor.execute(query)
    result = cursor.fetchone()
#    while (gradeline = result.fetch_row()

except mdb.Error as e:
    print "Error in query: %s" % query
    sys.exit(1)


print "there are %s grades at NES." % result

if connection:
   connection.close()


