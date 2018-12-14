#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()

form = cgi.FieldStorage()
gradeid = form.getvalue("grade")

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)


try:
    grade_q = "select grade from grades where id = " + gradeid
    cursor.execute(grade_q)
    grade = cursor.fetchone()
except mdb.Error as e:
    print "Error in query: %s" % grade_q
    sys.exit(1)


try: 
    minutes_q = "select "
    minutes_q += "(select sum(num_mins) from reading where studentid in "
    minutes_q +=   "(select id from students where classid in "
    minutes_q +=     "(select id from classes where gradeid = %s) " % gradeid
    minutes_q +=    ")"
    minutes_q +=  " ) + "
    minutes_q += "(select sum(num_mins) from classreading where classid in "
    minutes_q +=   "(select id from classes where gradeid = %s) " % gradeid
    minutes_q +=  ")" 
    cursor.execute(minutes_q)
    minutes = cursor.fetchone()
except mdb.Error as e:
    print "Error in query: %s" % minutes_q
    sys.exit(1)


    
print "Total reading time for %s: %d" % (str(grade[0]), minutes[0]) 


jrm.print_footer()
