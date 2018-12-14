#!/usr/bin/perl

my $file = $ARGV[0];

my ($classid, $teachername) = split('_', $file);
open (STUDLIST, $file) || die "Couldn't open $file: $!\n";
$classid++;

while (<STUDLIST>) {
    chomp;
#    my ($first, $last, $grade, $teach) = split(/\t+/);
    my ($teach, $grade, $first, $last) = split(/\t+/);
    print "insert into students values ('', $classid, \"$first $last\");\n\n";
}

close
