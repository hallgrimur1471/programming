package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	depth := 0
	pos := 0
	aim := 0

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		fields := strings.Fields(scanner.Text())
		op := fields[0]
		amount, err := strconv.Atoi(fields[1])
		if err != nil {
			log.Fatal(err)
		}

		switch op {
		case "forward":
			pos += amount
			depth += aim * amount
		case "down":
			aim += amount
		case "up":
			aim -= amount
		default:
			log.Fatal("Unexpected op")
		}
	}
	fmt.Println(pos * depth)
}
