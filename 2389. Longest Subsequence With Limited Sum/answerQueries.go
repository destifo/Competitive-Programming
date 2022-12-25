package answerQueries

import (
	"sort"
)

func findLongestSubsequence(target int, pf_sum *[]int) int {
	answer := 0

	lo := 0
	hi := len(*pf_sum) - 1

	for lo <= hi {
		mid := (lo + hi) / 2
		num := (*pf_sum)[mid]

		if num == target {
			return mid + 1
		} else if num < target {
			answer = mid + 1
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}

	return answer
}


// O(n + mlogn) time,
// O(n + m) space,
// Approach: prefix sum, binary search, 
func answerQueries(nums []int, queries []int) []int {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
	prefix_sum := make([]int, len(nums))
	tot := 0
	for i, num := range nums {
		tot += num
		prefix_sum[i] = tot
	}

	answer := make([]int, len(queries))
	for i, query := range queries {
		answer[i] = findLongestSubsequence(query, &prefix_sum)
	}

	return answer
}
