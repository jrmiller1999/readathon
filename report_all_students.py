#!/usr/bin/python

import MySQLdb as mdb, sys, cgi
import jrm_NESRAT_utils as jrm

jrm.print_header()

form = cgi.FieldStorage()
teacherid = form.getvalue("teacher")

try:
    connection = jrm.connect()
    student_cursor = connection.cursor()
    class_cursor = connection.cursor()
except mdb.Error, e:
    print_error(str(e.args[0])+" "+e.args[1])
    sys.exit(1)

try:
    student_reading_q = "select r.num_mins "
    student_reading_q += "from reading r, students s, classes c "
    student_reading_q += "where r.studentid = s.id and s.classid = c.id and c.teacherid = "
    student_reading_q += teacherid


#    student_reading_q = "select s.name, r.readdate, r.num_mins from reading r, students s "
#    student_reading_q += "where s.id = r.studentid and s.id = " 
#    student_reading_q += form.getvalue("student")

#    print "query will be " + student_reading_q
    student_cursor.execute(student_reading_q)
    student_times = student_cursor.fetchall()
except mdb.Error as e:
    print_error("Error with "+student_reading_q)
    sys.exit(1)

try:
    class_reading_q = "select cr.num_mins "
    class_reading_q += "from classes c, classreading cr "
    class_reading_q += "where cr.classid = c.id and c.teacherid = "
    class_reading_q += teacherid
    class_cursor.execute(class_reading_q)
    class_times = class_cursor.fetchall()

except mdb.Error as e:
    print_error("Error with "+class_reading_q)
    sys.exit(1)

try:
    teacher_q = "select name from teachers where id = " + teacherid
    class_cursor.execute(teacher_q)
    teacher = class_cursor.fetchone()
except mdb.Error as e:
    print_error("Error with "+teacher_q)
    sys.exit(1)

try:
    student_count_q = "select count(*) "
    student_count_q += "from students s, classes c "
    student_count_q += "where c.id = s.classid and c.teacherid = "
    student_count_q += teacherid
#    print "student_count_q is " + student_count_q
    class_cursor.execute(student_count_q)
    student_count = class_cursor.fetchone()
except mdb.Error as e:
    print_error("Error with "+student_count_q)
    sys.exit(1)

num_students = student_count[0]
total_time = 0




for student_time in student_times:
    total_time += student_time[0]


    
for class_time in class_times:
    total_time += class_time[0] * num_students

print "Total reading time for %s: %d" % (teacher[0], total_time) 

print "</table>\n"

jrm.print_footer()
