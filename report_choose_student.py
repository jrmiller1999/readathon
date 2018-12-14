#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()

print "<form name='grade' method='POST' action='report_time_student.py'>"

form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

try: 
    query = "select s.id, s.name from classes c, students s"
    query += " where c.teacherid = " + form.getvalue("teacher") + " and s.classid = c.id"
    #print query
    cursor.execute(query)
    #print form.getvalue("grade")
    students = cursor.fetchall()
except mdb.Error as e:
    print "Error in query: %s" % query
    sys.exit(1)


print "Choose your name, or <a href='report_all_students.py?teacher=%s'>click here</a> to report on the whole class:<br>" % form.getvalue("teacher").strip()
print "<select name='student'>"
for student in students:
    print "<option value='",student[0],"'>", student[1]
print "</select>"


print "<input type='submit'>"
print "</form>"

if connection:
    connection.close()

jrm.print_footer()
