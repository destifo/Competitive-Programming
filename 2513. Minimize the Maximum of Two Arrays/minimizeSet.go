package minimizeSet


import "math"

func gcd(a int, b int) int {
    for b != 0 {
        temp := b
        b = a % b
        a = temp
    } 
    return a
}


func isValidMax(num int, cnt1 int, cnt2 int, div1 int, div2 int) bool {
    arr1_len := num - (num/div1)
    arr2_len := num - (num/div2)
    lcm := div1*div2 / gcd(div1, div2)
    combined_len := num - (num/lcm)
    if arr1_len < cnt1 {
        return false
    }
    if arr2_len < cnt2 {
        return false
    }
    
    if combined_len < cnt1+cnt2 {
        return false
    }
    
    return true
}


// O(log(right)) time,
// O(1) space,
// Approach: math, binary search, 
func minimizeSet(divisor1 int, divisor2 int, uniqueCnt1 int, uniqueCnt2 int) int {
    left := 1
    right := math.MaxInt32
    ans := 1
    
    for left <= right {
        mid := left + (right-left)/2
        if isValidMax(mid, uniqueCnt1, uniqueCnt2, divisor1, divisor2) {
            ans = mid
            right = mid-1
        } else {
            left = mid+1
        }
    }
    
    return ans
}