package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {

	var n int
	fmt.Scan(&n)
	var s = make([]int, 0)
	for i := 0; i < n; i++ {
		var tmp string
		fmt.Scan(&tmp)
		res, _ := strconv.Atoi(tmp)
		s = append(s, res)

	}
	sort.Ints(s)
	fmt.Println(s[n-1] - s[0] - n + 1)

}
