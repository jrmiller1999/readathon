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

try:
    studentid = form.getvalue("student")
    studid = studentid.strip()
    query = "select name from students"
    query += " where id = " + studentid
    #print query
    cursor.execute(query)
    #print form.getvalue("grade")
    students = cursor.fetchall()
except mdb.Error as e:
    print "Error in query: %s" % query
    sys.exit(1)

for student in students: #better not run more than once, or something broke
    print "<h2>Entering time for ", student[0], "</h2>"

print "<h4>To edit a previous entry instead, use <a href='edit_find_times.py?student=%s'>this page</a></h4>" % studid
print "<form method='POST' action='confirm_time.py'>"
print "<input type='hidden' name='student' value='%s'>" % studid
print "Date of reading: <select name='date'>"
print jrm.date_select()
print "</select><br>"
print "Amount of time read: <select name='hours'>", jrm.hour_select(), "</select> hrs"
print "<select name='mins'>", jrm.minute_select(), "</select> min<br>"

print "<input type='submit'> <input type='reset'>"
print "</form>"


if connection:
    connection.close()

jrm.print_footer()
