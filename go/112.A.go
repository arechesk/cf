package main

import (
	"fmt"
	"strings"
)

func main() {
	var a string
	var b string
	fmt.Scan(&a)
	fmt.Scan(&b)
	a = strings.ToUpper(a)
	b = strings.ToUpper(b)
	if a < b {
		fmt.Println(-1)
	} else if a > b {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
