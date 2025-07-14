package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int) // value -> index

	for i, num := range nums {
		complement := target - num

		if idx, found := seen[complement]; found {
			return []int{idx, i}
		}

		seen[num] = i


	return nil
}

func main() {
	nums := []int{5, 7, 3, 2}
	target := 9

	result := twoSum(nums, target)
	fmt.Println(result) // Output: [1 3]
}
