#!/usr/bin/python

import MySQLdb as mdb, sys

print "Content-type: text/html\n\n"

print "<h1>hello world</h1>"

try: 
    con = mdb.connect ('localhost', 'nes_read', 'r3adingr0cks!', 'readathon')
    con.query("select count(*) from grades")

    result = con.use_result()
    print "there are %s grades at NES." % result.fetch_row()[0]

except mdb.Error, e:
    print "Error %d: %s" % (str(e.args[0]), e.args[1])
    sys.exit(1)

