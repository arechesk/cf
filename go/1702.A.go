package main

import (
	"fmt"
	"math/big"
)

func main() {
	var t int
	fmt.Scan(&t) // read number of test cases

	for i := 0; i < t; i++ {
		var s string
		fmt.Scan(&s) // read the number as string

		// Convert to big.Int
		n := new(big.Int)
		n.SetString(s, 10)

		// Compute 10^(len(s)-1)
		exp := int64(len(s) - 1)
		power := new(big.Int).Exp(big.NewInt(10), big.NewInt(exp), nil)

		// result = n - power
		result := new(big.Int).Sub(n, power)

		// Output result
		fmt.Println(result)
	}
}
