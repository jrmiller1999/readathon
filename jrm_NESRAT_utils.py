import MySQLdb as mdb, sys

## Connect to the Readathon database
def connect():
    try:

        con = mdb.connect ('localhost', 'navigaz2_nesread', 'readingrocks2015', 'navigaz2_readathon2015')
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
    print "<h5>Built by Jonathan Miller, July 2015</h5>"
    print "</body></html>"


## generate a list of dates in a select form element to choose from, 
## rather than having to validate user entries
def date_select():
    date_list = ""
    date_list += "<option value='' selected>Choose a date..."
    date_list += "<option value='2016-01-20'>Jan 20, 2016"
    date_list += "<option value='2016-01-21'>Jan 21, 2016"
    date_list += "<option value='2016-01-22'>Jan 22, 2016"
    date_list += "<option value='2016-01-23'>Jan 23, 2016"
    date_list += "<option value='2016-01-24'>Jan 24, 2016"
    date_list += "<option value='2016-01-25'>Jan 25, 2016"
    date_list += "<option value='2016-01-26'>Jan 26, 2016"
    date_list += "<option value='2016-01-27'>Jan 27, 2016"
    date_list += "<option value='2016-01-28'>Jan 28, 2016"
    date_list += "<option value='2016-01-29'>Jan 29, 2016"
    date_list += "<option value='2016-01-30'>Jan 30, 2016"
    date_list += "<option value='2016-01-31'>Jan 31, 2016"
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
