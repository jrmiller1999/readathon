#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()


print "<form name='grade' method='POST' action='add_time_class.py'>"

form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print_error(str(e.args[0])+": "+e.args[1])
    sys.exit(1)


try: 
    query = "select t.id, t.name from teachers t, classes c"
    query += " where c.gradeid = " + form.getvalue("grade") + " and c.teacherid = t.id"
    #print query
    cursor.execute(query)
    #print form.getvalue("grade")
    teachers = cursor.fetchall()
except mdb.Error as e:
    print_error("Error with "+upd_query)
    sys.exit(1)

print "Choose your teacher:"
print "<select name='teacher'>"
for teacher in teachers:
    print "<option value='",teacher[0],"'>", teacher[1]
print "</select>"


print "<input type='submit'>"
print "</form>"

if connection:
    connection.close()

jrm.print_footer()
