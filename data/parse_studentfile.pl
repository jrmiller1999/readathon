#!/bin/perl

# parse a file in the format <teacher_name> <grade_id> <firstname> <lastinitial> and
# make files to load into the tables:
# teachers table: <id>, <name> 
# grades table: <id>, <grade>  (this isn't actually added from this script; it's part of the db structure)
#     grade_id is -1 for pre-k; 0 for k; 1-5 for grades 1-5, respectively; and 9 for system-level
# classes table:  <id>, <gradeid>, <teacherid>, <passwd>
# students table: <id>, <classid>, <name>
#
### Jonthan Miller, 11 Jan 2019


## print "insert into classes values ('', '', $teacherid, '$teach');\n"
## print "insert into students values ('', $classid, \"$first $last\");\n\n";
## print "insert into teachers values ('', '$teach');\n"

my $datafile = $ARGV[0];
my %teachers, %classes, %students; # hashes to hold the data until being printed out
## $teacher{$id} = $name
## $classes{$id} = "$gradeid:$teacherid:$passwd"
## $students{$id} = "$classid:$firstname $lastinitial"

open (DATA, $datafile) || die "Unable to open $datafile: $!\n";

my $currentteacher = "--";
my $classstring = "";
my $studentname = "";
my $teacherid = -1;
my $studentid = 0;
my $classid = -1;
#print "reading $datafile...\n";
while (<DATA>) {
#    print;
    chomp;
    my ($teacher, $gradeid, $first, $last) = split;
#    print "t: $teacher; c: $currentteacher\n";
    if ($teacher !~ $currentteacher) {     # we're onto a new teacher, and a new class
#	print "incrementing teacher and class\n";
	$teacherid++;                      # get the next teacher ID
	$classid++;                        # get the next teacher ID
	$teachers{$teacherid} = $teacher;  # add the new teacher to the teachers array
	$currentteacher = $teacher;        # update the current teacher name
	$classstring = "$gradeid:$teacherid:$teacher";
                                           # passwd is teacher's name
	$classes{$classid} = $classstring; # add the new class to the classes array
    }
    # whether we have a new class or not, we have a new student
    $studentname = "$first $last";
    $students{$studentid} = "$classid:$studentname"; # add the new student to the students array
    $studentid++;                                    # get the next student ID
}

# array @teachers, @classes, and @students should now have the data in them; it's time to write out the
# insert strings

foreach my $teacher ( keys %teachers ) {
    print "insert into teachers values ($teacher, '$teachers{$teacher}');\n";
}
print "\n";
foreach my $class ( keys %classes ) {
    my ($gradeidins, $teacheridins, $passwd) = split(/:/, $classes{$class});
    print "insert into classes values ($class, $gradeidins, $teacheridins, '$passwd');\n";
}
print "\n";
foreach my $student ( keys %students ) {
    my ($classidins, $name) = split(/:/, $students{$student});
    print "insert into students values ($student, $classidins, \"$name\");\n";
}
close
