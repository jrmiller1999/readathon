#!/usr/bin/python

import MySQLdb as mdb, sys, cgi, os, time, datetime
import jrm_NESRAT_utils as jrm

jrm.print_header()

form = cgi.FieldStorage()

try:
    connection = jrm.connect()
    cursor = connection.cursor()
except mdb.Error, e:
    print_error(str(e.args[0])+": "+e.args[1])
    sys.exit(1)

# audit info
ipaddr = cgi.escape(os.environ["REMOTE_ADDR"])
ts = time.time()
audit_ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

ins_studid = str(form.getvalue("insert_studid"))
ins_readdate = str(form.getvalue("insert_readdate"))
ins_mins = str(form.getvalue("insert_mins"))
ins_query = "insert into reading values ('', %s, '%s', %s, '%s', '%s')" % (ins_studid, ins_readdate, ins_mins, ipaddr, audit_ts)
print "query is %s " % ins_query
try: 
    result = cursor.execute(ins_query)
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
