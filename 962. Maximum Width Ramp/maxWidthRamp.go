package MaxWidthRamp

import "math"

// O(n) time, 2n practically
// O(n) space,
// Approach: stack, monotonic stack
func maxWidthRamp(nums []int) int {
    
    stack := []int{}
    
    for i, val := range nums {
        if len(stack) == 0 || nums[stack[len(stack)-1]] >= val {
            stack = append(stack, i)
        }
    }
    
    maxWidth := 0
    for i := len(nums)-1; i >= 0; i-- {
        for len(stack) > 0 && nums[i] >= nums[stack[len(stack)-1]] {
            rampStartIndex := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            currWidth := float64(i-rampStartIndex)
            maxWidth = int(math.Max(float64(maxWidth), currWidth))
        }
    }
    
    return maxWidth
}

// O(n) time, 2n practically
// O(n) space,
// Approach: two pointers
func maxWidthRamp2(nums []int) int {
    
    // [8,8,8,5,5,5]
    rightMax := make([]int, len(nums))
    rightMax[len(nums)-1] = nums[len(nums)-1]
    for i := len(nums)-2; i >= 0; i-- {
        if rightMax[i+1] > nums[i] {
            rightMax[i] = rightMax[i+1]
        } else {
            rightMax[i] = nums[i]
        }
    }
    
    maxWidth := float64(0)
    left, right := 0, 0
    for right < len(nums) {
        for nums[left] > rightMax[right] {
            left += 1
        }
        currWidth := float64(right-left)
        maxWidth = math.Max(maxWidth, currWidth)
        right += 1
    }
    
    return int(maxWidth)
}
