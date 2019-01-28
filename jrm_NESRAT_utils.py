import MySQLdb as mdb, sys, os

## Connect to the Readathon database
def connect():
    try:
        con = mdb.connect ('localhost', 'nes_read', 'r3adingr0cks!', 'readathon')
#        curs = con.cursor()


    except mdb.Error, e:
        print_error(str(e.args[0])+": "+e.args[1])
        sys.exit(1)
        
    return con

## print the header, found at the top of each page
def print_header():
    print "Content-type: text/html\n\n"
    print "<html><title>Northside Elementary Readathon</title>"
    print "<body>"
    print "<div  align='center'><img src='/images/Full_RAT_Logo_2019.png'></div><br><br>"

## advise on errors
def print_error(errormsg):
    print "We're sorry! There's been an error.<br>"
    print "Please send this the following information, along with a brief description of what you're trying to do,<br>"
    print "to <a href='mailto:jrmiller1999@gmail.com'>the administrator</a> for investigation.<br>"
    print errormsg

## print the footer, found at the bottom of each page
def print_footer():
    print "<hr width='75%'>"
    print "<font size='-1'><a href='/cgi-bin/readathon/start.py'>Start over</a> on an student entry<br>"  
    print "<a href='/cgi-bin/readathon/start_class.py'>Start over</a> on an class entry<br></font>"  
    print "<h5>Built by Jonathan Miller, July 2015; updated Jan 2017; updated Jan 2019</h5>"
    print "</body></html>"


## generate a list of dates in a select form element to choose from, 
## rather than having to validate user entries
def date_select():
    date_list = ""
    date_list += "<option value='' selected>Choose a date..."
    date_list += "<option value='2019-02-01'>Feb 1, 2019"
    date_list += "<option value='2019-02-02'>Feb 2, 2019"
    date_list += "<option value='2019-02-03'>Feb 3, 2019"
    date_list += "<option value='2019-02-04'>Feb 4, 2019"
    date_list += "<option value='2019-02-05'>Feb 5, 2019"
    date_list += "<option value='2019-02-06'>Feb 6, 2019"
    date_list += "<option value='2019-02-07'>Feb 7, 2019"
    date_list += "<option value='2019-02-08'>Feb 8, 2019"
    date_list += "<option value='2019-02-09'>Feb 9, 2019"
    date_list += "<option value='2019-02-10'>Feb 10, 2019"
    return date_list

## a couple functions to make hour and minute drop-downs; 
## minutes will be in 5 minute increments
def hour_select():
    hour_list = ""
    hour_list += "<option value='0' selected>0"
    hour_list += "<option value='1'>1"
    hour_list += "<option value='2'>2"
    hour_list += "<option value='3'>3"
    hour_list += "<option value='4'>4"
    hour_list += "<option value='5'>5"
    return hour_list

def minute_select():
    min_list = ""
    for min in range (0, 60, 5):
        min_list += "<option value='%s'>%s" % (min, min)
    return min_list
