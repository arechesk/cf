<?php
$t = (int) trim(fgets(STDIN));

while ($t-- > 0) {
    $n = trim(fgets(STDIN));            // read number as string
    $len = strlen($n);
    // compute 10^(len-1) using BCMath for arbitrary precision
    $power = bcpow('10', (string) ($len - 1));
    $result = bcsub($n, $power);
    echo $result . "\n";
}
?>
