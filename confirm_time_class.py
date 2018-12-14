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


hours = int(form.getvalue("hours"))
mins = int(form.getvalue("mins"))
teacherid = str(form.getvalue("teacher"))
readdate = form.getvalue("date")
classpassword = str(form.getvalue("classpwd"))
total_min = hours*60 + mins

try:
    query = "select t.name, c.id, c.passwd from classes c, teachers t where c.teacherid = t.id and t.id = " + teacherid
    cursor.execute(query)
    classes = cursor.fetchall()
except mdb.Error as e:
    print "Error in query: %s" % query
    sys.exit(1)

for myclass in classes: #better not run more than once, or something broke
    teachname = myclass[0]
    classid = myclass[1]
    passwd = myclass[2]

if classpassword != passwd:
    print "The provided password does not match the class password. Please go back and try again."
    sys.exit(1)

print "Please confirm you wish to add the following entry for %s:<br> " % teachname
print "Date: %s<br>" % readdate
print "Time: %s hours, %s minutes (%s minutes total)<br>" % (hours, mins, total_min)
print "<form method='POST' action='add_and_report_class.py'>"
print "<input type='hidden' name='insert_classid' value='%s'>" % classid
print "<input type='hidden' name='insert_readdate' value='%s'>" % readdate
print "<input type='hidden' name='insert_mins' value='%s'>" % total_min
print "<input type='submit' value='Confirm!'><br>"
print "If you see an error, please hit the Back button and change your information."
print "</form>"


if connection:
    connection.close()

jrm.print_footer()
