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

#ins_studid = str(form.getvalue("insert_studid"))
#ins_readdate = str(form.getvalue("insert_readdate"))
#ins_mins = str(form.getvalue("insert_mins"))
#ins_query = "insert into reading values ('', %s, '%s', %s)" % (ins_studid, ins_readdate, ins_mins)
upd_readid = str(form.getvalue("classreadingid"))
upd_mins = str(form.getvalue("newmins"))
upd_passwd = str(form.getvalue("classpwd"))

pwd_query = "select cr.id, c.passwd from classes c, classreading cr where cr.classid = c.id and cr.id = " + upd_readid

try:
    cursor.execute(pwd_query)
    passres = cursor.fetchall()
except mdb.Error as res_e:
    print_error("Error with "+pwd_query)
    sys.exit(1)

for passwd in passres:
    if passwd[1] != upd_passwd:
        print "The provided password does not match the class password. Please go back and try again."
        sys.exit(1)
        

#upd_query = "update classreading set num_mins = '%s' where id = '%s'" % (upd_mins, upd_readid)

print "query is %s " % upd_query
try: 
    result = cursor.execute(upd_query)
    #print form.getvalue("grade")
    if result:
        print "Successfully added time!"
    else:
        print "There was a problem."

except mdb.Error as e:
    print_error("Error with "+upd_query)
    sys.exit(1)


if connection:
    connection.close()

jrm.print_footer()
