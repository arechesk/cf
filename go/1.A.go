package main

import (
	"fmt"
)

func main() {
	var n int64
	var m int64
	var a int64
	var r int64
	var k int64
	fmt.Scan(&n, &m, &a)
	if n%a == 0 {
		r = int64(n / a)
	} else {
		r = int64(n/a) + 1
	}
	if m%a == 0 {
		k = int64(m / a)
	} else {
		k = int64(m/a) + 1
	}
	fmt.Print(r * k)

}
