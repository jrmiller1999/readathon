#!/usr/bin/python

import MySQLdb as mdb, sys, cgi, os, time, datetime
import jrm_NESRAT_utils as jrm

jrm.print_header()

form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print_error(str(e.args[0])+" "+e.args[1])
    sys.exit(1)

# audit info
ipaddr = cgi.escape(os.environ["REMOTE_ADDR"])
ts = time.time()
audit_ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

#ins_studid = str(form.getvalue("insert_studid"))
#ins_readdate = str(form.getvalue("insert_readdate"))
#ins_mins = str(form.getvalue("insert_mins"))
#ins_query = "insert into reading values ('', %s, '%s', %s)" % (ins_studid, ins_readdate, ins_mins)
upd_readid = str(form.getvalue("readingid"))
upd_mins = str(form.getvalue("newmins"))
upd_query = "update reading set num_mins = '%s', ipaddr = '%s', audit_ts = '%s' where id = '%s'" % (upd_mins, ipaddr, audit_ts, upd_readid)

#print "query is %s " % upd_query
try: 
    result = cursor.execute(upd_query)
    #print form.getvalue("grade")
    if result:
        print "Successfully updated time!"
    else:
        print "There was a problem."

except mdb.Error as e:
    print_error("Error with "+upd_query)
    sys.exit(1)


if connection:
    connection.close()

jrm.print_footer()
