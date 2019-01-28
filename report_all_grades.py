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
    print_error(str(e.args[0])+" "+e.args[1])
    sys.exit(1)


try:
    grade_q = "select id from grades"
    cursor.execute(grade_q)
    grades = cursor.fetchall()
except mdb.Error as e:
    print_error("Error with "+grade_q)
    sys.exit(1)

total_time = 0
for gradeid in grades:
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
        print_error("Error with "+minutes_q)
        sys.exit(1)

    if minutes[0] != None:
        total_time += minutes[0]
    
print "Total reading time for Northside Elementary: %d" % total_time


jrm.print_footer()
