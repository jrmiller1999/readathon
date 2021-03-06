#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()


form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print_error(str(e.args[0])+": "+e.args[1])
 #    print "Error %d: %s" % (str(e.args[0]), e.args[1])
    sys.exit(1)

try: 
    query = "select t.name, cr.readdate, cr.num_mins, cr.id from classreading cr, teachers t, classes c"
    query += " where t.id = " + form.getvalue("teacher") + " and t.id = c.teacherid and c.id = cr.classid"
    #print query
    cursor.execute(query)
    #print form.getvalue("grade")
    readentries = cursor.fetchall()
except mdb.Error as e:
    print_error("Error with "+query)
    sys.exit(1)

print "<table border='1'><tr>"
print "<td colspan='6'>Select an entry to edit:</td>"
print "</tr>\n"
print "<tr><th>Class Name</th><th>Date</th><th>Num. Minutes</th><th>New Minutes</th><th>Pasword</th><th> </th></tr>\n"
for entry in readentries:
    print "<tr>\n"
    print "<form name='grade%d' method='POST' action='edit_time_class.py'>" % entry[3]
    print "<input type='hidden' name='classreadingid' value='%d'>" % entry[3]
    print "<td>" + entry[0] + "</td>\n"
    print "<td>%s</td>\n" % str(entry[1])
    print "<td>%d</td>\n" % entry[2]
    print "<td><input type='text' size='2' name='newmins'></td>\n"
    print "<td><input type='password' name='classpwd'></td>\n"
    print "<td><input type='submit'>\n</td>"
#    print "<td><a href='edit_time.py?" + str(entry[3]) + "'>Edit</a></td>\n"
    print "</form>"
    print "</tr>\n"

print "</table>\n"


if connection:
    connection.close()

jrm.print_footer()
