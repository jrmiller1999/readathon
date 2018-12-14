#!/usr/bin/python

import MySQLdb as mdb, sys
import jrm_NESRAT_utils as jrm

jrm.print_header()

print "<form name='grade' method='POST' action='/cgi-bin/readathon/report_choose_teacher.py'>"

try: 
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)


try:
    query = "select id, grade from grades"
    cursor.execute(query)
    grades = cursor.fetchall()

except mdb.Error as e:
    print "Error in query: %s" % query
    sys.exit(1)

print "Choose your grade, or <a href='report_all_grades.py'>click here</a> to report on the whole school:<br>"
print "<select name='grade'>"
for grade in grades:
    print "<option value='",grade[0],"'>", grade[1]

print "</select>"


print "<input type='submit'>"
print "</form>"

if connection:
    connection.close()

jrm.print_footer()
