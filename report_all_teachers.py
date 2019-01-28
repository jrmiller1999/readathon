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
    grade_q = "select grade from grades where id = " + gradeid
    cursor.execute(grade_q)
    grade = cursor.fetchone()
except mdb.Error as e:
    print_error("Error with "+grade_q)
    sys.exit(1)

try: 
    classes_q = "select id from classes where gradeid = " + gradeid
    cursor.execute(classes_q)
    classes = cursor.fetchall()
except mdb.Error as e:
    print_error("Error with "+classes_q)
    sys.exit(1)

try: 
    minutes_q = "select "
    minutes_q += "(select sum(num_mins) from reading where studentid in "
    minutes_q +=   "(select id from students where classid in "
    minutes_q +=     "(select id from classes where gradeid = %s) " % gradeid
    minutes_q +=    ")"
    minutes_q += ")"
#    minutes_q +=  " ) + "
#    minutes_q += "(select sum(num_mins) from classreading where classid in "
#    minutes_q +=   "(select id from classes where gradeid = %s) " % gradeid
#    minutes_q +=  ")" 
##    print "query is %s" % minutes_q
    cursor.execute(minutes_q)
    minutes = cursor.fetchone()
except mdb.Error as e:
    print_error("Error with "+minutes_q)
    sys.exit(1)

total_min = minutes[0]

for myclass in classes:
    try: 
        numstudents_q = "select count(*) from students where classid = %d " % myclass
        cursor.execute(numstudents_q)
        numstudents = cursor.fetchone()
    except mdb.Error as e:
        print_error("Error with "+grade_q)
        sys.exit(1)

    try:
        classreading_q = "select sum(num_mins) from classreading where classid = %d " % myclass
        cursor.execute(classreading_q)
        classreading = cursor.fetchone()
    except mdb.Error as e:
        print_error("Error with "+grade_q)
        sys.exit(1)

#    print myclass[0]
    if cursor.rowcount > 0:
#        print "<br>rows returned %d " % cursor.rowcount
        classtotal = int(classreading[0]) * int(numstudents[0])
#        print "classreading %d <br><br> " % classreading
#        print "numstudents %d <br><br>"%  numstudents
        total_min += classtotal
    
#print "Total reading time for %s: %d" % (str(grade[0]), minutes[0]) 
print "Total reading time for Grade %s: %d" % (str(grade[0]), total_min) 


jrm.print_footer()
