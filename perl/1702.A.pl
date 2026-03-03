#!/usr/bin/perl
use strict;
use warnings;
use bigint;   # enable arbitrary-precision integers

my $t = <STDIN>;
chomp $t;

for (1 .. $t) {
    my $n_str = <STDIN>;
    chomp $n_str;

    my $len   = length $n_str;
    my $power = 10 ** ($len - 1);   # bigint handles huge exponents
    my $n     = $n_str;              # automatically converted to bigint

    print $n - $power, "\n";
}
