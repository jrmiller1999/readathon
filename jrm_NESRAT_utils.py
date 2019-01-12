import MySQLdb as mdb, sys

## Connect to the Readathon database
def connect():
    try:
        con = mdb.connect ('localhost', 'nes_read', 'passwordgoeshere', 'readathon')
#        curs = con.cursor()


    except mdb.Error, e:
        print "Error in connection to %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
        
    return con

## print the header, found at the top of each page
def print_header():
    print "Content-type: text/html\n\n"
    print "<html><title>Northside Elementary Readathon</title>"
    print "<body>"
    print "<h1>This is a header imported on all pages.</h1>"

## print the footer, found at the bottom of each page
def print_footer():
    print "<h5>Built by Jonathan Miller, July 2015; updated Jan 2017; updated Jan 2019</h5>"
    print "</body></html>"


## generate a list of dates in a select form element to choose from, 
## rather than having to validate user entries
def date_select():
    date_list = ""
    date_list += "<option value='' selected>Choose a date..."
    date_list += "<option value='2017-02-03'>Feb 3, 2017"
    date_list += "<option value='2017-02-04'>Feb 4, 2017"
    date_list += "<option value='2017-02-05'>Feb 5, 2017"
    date_list += "<option value='2017-02-06'>Feb 6, 2017"
    date_list += "<option value='2017-02-07'>Feb 7, 2017"
    date_list += "<option value='2017-02-08'>Feb 8, 2017"
    date_list += "<option value='2017-02-09'>Feb 9, 2017"
    date_list += "<option value='2017-02-10'>Feb 10, 2017"
    date_list += "<option value='2017-02-11'>Feb 11, 2017"
    date_list += "<option value='2017-02-12'>Feb 12, 2017"
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
