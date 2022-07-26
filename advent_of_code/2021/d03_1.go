package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	num_binaries := 0
	var bit_counts []int
	for scanner.Scan() {
		byte_string := scanner.Text()
		if len(bit_counts) == 0 {
			bit_counts = make([]int, len(byte_string))
		}
		b, err := strconv.ParseInt(byte_string, 2, 0)
		if err != nil {
			log.Fatal("Failed to parse input byte")
		}
		for i := 0; b > 0; i++ {
			if b&1 == 1 {
				bit_counts[i] += 1
			}
			b = b >> 1
		}
		num_binaries += 1
	}
	gamma_rate := 0
	for j, _ := range bit_counts {
		i := len(bit_counts) - j - 1
		gamma_rate = gamma_rate << 1
		if bit_counts[i] > num_binaries/2 {
			gamma_rate = gamma_rate | 1
		}
	}
	epsilon_rate := gamma_rate ^ (int(math.Pow(2, float64(len(bit_counts)))) - 1)
	fmt.Println(gamma_rate * epsilon_rate)
}
