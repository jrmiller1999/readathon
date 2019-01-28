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

teacherid = form.getvalue("teacher")
teach = teacherid.strip()

print "<h4>To edit a previous entry instead, use <a href='edit_find_times_class.py?teacher=%s'>this page</a></h4>" % teach
print "<form method='POST' action='confirm_time_class.py'>"
print "<input type='hidden' name='teacher' value='%s'>" % teach
print "Date of reading: <select name='date'>"
print jrm.date_select()
print "</select><br>"
print "Amount of time read: <select name='hours'>", jrm.hour_select(), "</select> hrs"
print "<select name='mins'>", jrm.minute_select(), "</select> min<br>"
print "Class password: <input type='password' name='classpwd'><br>"

print "<input type='submit'> <input type='reset'>"
print "</form>"


if connection:
    connection.close()

jrm.print_footer()
