package main

import (
	"fmt"
)

func main() {
	var a []int
	var curr int
	for {
		if _, e := fmt.Scanln(&curr); e != nil {
			break
		}
		a = append(a, curr)
	}

	count := 0
	for i := range a {
		if i >= 3 && sum(a[i-2:i+1]) > sum(a[i-3:i]) {
			count += 1
		}
	}

	fmt.Println(count)
}

func sum(b []int) int {
	s := 0
	for i := 0; i < len(b); i++ {
		s += b[i]
	}
	return s
}
