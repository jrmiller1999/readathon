#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()

form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print_error(str(e.args[0])+" "+e.args[1])
    sys.exit(1)


hours = int(form.getvalue("hours"))
mins = int(form.getvalue("mins"))
studid = str(form.getvalue("student"))
readdate = form.getvalue("date")
total_min = hours*60 + mins

try:
    query = "select name from students where id = " + studid
    cursor.execute(query)
    students = cursor.fetchall()
except mdb.Error as e:
    print_error("Error with "+query)
    sys.exit(1)

for student in students: #better not run more than once, or something broke
    studname = student[0]

print "Please confirm you wish to add the following entry for %s:<br> " % studname
print "Date: %s<br>" % readdate
print "Time: %s hours, %s minutes (%s minutes total)<br>" % (hours, mins, total_min)
print "<form method='POST' action='add_and_report.py'>"
print "<input type='hidden' name='insert_studid' value='%s'>" % studid
print "<input type='hidden' name='insert_readdate' value='%s'>" % readdate
print "<input type='hidden' name='insert_mins' value='%s'>" % total_min
print "<input type='submit' value='Confirm!'><br>"
print "If you see an error, please hit the Back button and change your information."
print "</form>"


if connection:
    connection.close()

jrm.print_footer()
