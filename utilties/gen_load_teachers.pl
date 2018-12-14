#!/usr/bin/perl

my $file = $ARGV[0];

my ($classid, $rest1) = split(/_/, $file);
my ($teach, $suffix) = split(/\./, $rest1);

print "insert into teachers values ('', '$teach');\n"
