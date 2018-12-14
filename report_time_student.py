#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()

form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    student_cursor = connection.cursor()
    class_cursor = connection.cursor()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

try:
    student_reading_q = "select s.name, r.readdate, r.num_mins from reading r, students s "
    student_reading_q += "where s.id = r.studentid and s.id = " 
    student_reading_q += form.getvalue("student")

#    print "query will be " + student_reading_q
    student_cursor.execute(student_reading_q)
    student_times = student_cursor.fetchall()
except mdb.Error as e:
    print "Error in query: %s" % student_reading_q
    sys.exit(1)

try:
    class_reading_q = "select t.name, cr.readdate, cr.num_mins "
    class_reading_q += "from teachers t, students s, classes c, classreading cr "
    class_reading_q += "where s.classid = c.id and c.teacherid = t.id and cr.classid = c.id "
    class_reading_q += " and s.id = " + form.getvalue("student")
    class_cursor.execute(class_reading_q)
    class_times = class_cursor.fetchall()


    
except mdb.Error as e:
    print "Error in query: %s" % class_reading_q
    sys.exit(1)

total_time = 0
current_date = ''
bgcolors={1: '#FFCC00', -1: '#66CCFF'}
print "<table border='1'>\n"
print "<tr><th>Student Name</th><th>Date</th><th>Num. Minutes</th></tr>\n"
color=1
for student_time in student_times:
    if current_date != student_time[1]:
        current_date = student_time[1]
        color*=-1
#        print "different: %s, %s\n" % (current_date, student_time[1])
#        current_date = 
#    else:
#        print "same: %s, %s\n" % (current_date, student_time[1])

    print "<tr bgcolor='%s'>\n" % bgcolors[color]
    print "<td>%s</td>\n" % student_time[0]
    print "<td>%s</td>\n" % student_time[1]
    print "<td>%s</td>\n" % student_time[2]
    print "</tr>\n"
    total_time += student_time[2]
    
print "<tr><td colspan='2'><b>STUDENT SUB-TOTAL</b></td><td>%d</td></tr>\n" % total_time
print "<tr><th>Class Name</th><th>Date</th><th>Num. Minutes</th></tr>\n"
current_date = ''
for class_time in class_times:
    if current_date != class_time[1]:
        color*=-1
        current_date = class_time[1]
    print "<tr bgcolor='%s'>\n" % bgcolors[color]
    print "<td>%s</td>\n" % class_time[0]
    print "<td>%s</td>\n" % class_time[1]
    print "<td>%s</td>\n" % class_time[2]
    print "</tr>\n"
    total_time += class_time[2]
print "<tr><td colspan='2'><b>TOTAL</b></td><td>%d</td></tr>\n" % total_time

print "</table>\n"

jrm.print_footer()
