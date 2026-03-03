import std.stdio;
import std.string;
import std.conv;

void main() {
    int t = readln().strip().to!int;   // number of test cases
    foreach (_; 0 .. t) {
        string s = readln().strip();   // read number as string (to get length)
        long n = s.to!long;             // convert to integer
        long power = 1;
        foreach (i; 1 .. s.length) {    // compute 10^(len-1)
            power *= 10;
        }
        writeln(n - power);              // output result
    }
}
