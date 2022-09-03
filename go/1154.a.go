package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {

	var s = make([]int, 0)
	for i := 0; i < 4; i++ {
		var tmp string
		fmt.Scan(&tmp)
		res, _ := strconv.Atoi(tmp)
		s = append(s, res)
	}
	sort.Ints(s)
	fmt.Println(s[3]-s[0], s[3]-s[1], s[3]-s[2])

}
