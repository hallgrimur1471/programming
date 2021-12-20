package main

import (
	"fmt"
	"math"
)

func main() {
	var curr int
	last := math.MaxInt
	count := 0

	for {
		if _, e := fmt.Scanln(&curr); e != nil {
			break
		}
		if curr > last {
			count++
		}

		last = curr
	}
	fmt.Println(count)
}
