#!/usr/bin/python

import MySQLdb as mdb, sys
import jrm_NESRAT_utils as jrm

jrm.print_header()

print "This page sequence will add time for the entire class.  If you need to look up a student for<br>"
print "individual reading times, use <a href='choose_teacher.py'>this page</a><br><br>"


print "<form name='grade' method='POST' action='/cgi-bin/readathon/choose_teacher_class.py'>"

try: 
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print_error(str(e.args[0])+": "+e.args[1])
    sys.exit(1)


try:
    query = "select id, grade from grades"
    cursor.execute(query)
    grades = cursor.fetchall()

except mdb.Error as e:
    print_error("Error with "+query)
    sys.exit(1)

print "Choose your grade:"
print "<select name='grade'>"
for grade in grades:
    print "<option value='",grade[0],"'>", grade[1]

print "</select>"


print "<input type='submit'>"
print "</form>"

if connection:
    connection.close()

jrm.print_footer()
