#!/usr/bin/python

import _mysql, sys

print "Content-type: text/html\n\n"

print "<h1>hello world</h1>"

try: 
    con = _mysql.connect ('localhost', 'nes_read', 'readingrocks', 'readathon2015')
    con.query("select count(*) from grades")

    result = con.use_result()
    print "there are %s grades at NES." % result.fetch_row()[0]

except _mysql.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

