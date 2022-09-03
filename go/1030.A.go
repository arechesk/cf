package main

import (
	"fmt"
)

func main() {

	var n, b int
	fmt.Scan(&n)
	for i := 0; i < n; i++ {
		fmt.Scan(&b)
		if b == 1 {
			fmt.Println("HARD")
			return
		}
	}
	fmt.Println("EASY")

}
