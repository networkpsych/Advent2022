package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	signal := make([]int, 2)
	beacon := make([]int, 2)
	distance := make([]int, 10)
	i := 0
	f, err := os.Open("beacons.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()
	file := bufio.NewScanner(f)

	for file.Scan() {
		tmp := strings.Split(file.Text(), " | ")
		sig := strings.Split(tmp[0], ",")
		bea := strings.Split(tmp[1], ",")
		signal[0], _ = strconv.Atoi(sig[0])
		signal[1], _ = strconv.Atoi(sig[1])
		beacon[0], _ = strconv.Atoi(bea[0])
		beacon[1], _ = strconv.Atoi(bea[1])
		if beacon[1] == 2000000 {
			fmt.Printf("Distance: %d\n", sig_beac(signal, beacon))
			fmt.Printf("Signal coor: X=%d, Y=%d\t", signal[0], signal[1])
			fmt.Printf("Beacon coor: X=%d, Y=%d\n\n", beacon[0], beacon[1])
			distance[i] = sig_beac(signal, beacon)
			i += 1
		}
	}
	fmt.Println(distance)
}

func sig_beac(q, p []int) int {
	// q == Signal
	// p == Beacon
	distance := (p[0] - q[0]) + (p[1] - q[1])
	if distance < 0 {
		distance = distance * -1
	}
	return distance
}
