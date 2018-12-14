#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()

form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

ins_classid = str(form.getvalue("insert_classid"))
ins_readdate = str(form.getvalue("insert_readdate"))
ins_mins = str(form.getvalue("insert_mins"))
ins_query = "insert into classreading values ('', %s, '%s', %s, '')" % (ins_classid, ins_readdate, ins_mins)
print "query is %s " % ins_query
try: 
    result = cursor.execute(ins_query)
    #print form.getvalue("grade")
    if result:
        print "Successfully added time!"
    else:
        print "There was a problem."

except mdb.Error as e:
    print "Error in query: %s" % ins_query
    sys.exit(1)


if connection:
    connection.close()

jrm.print_footer()
