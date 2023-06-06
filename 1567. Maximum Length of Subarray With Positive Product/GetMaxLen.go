package getMaxLen


// O(n) time,
// O(1) space,
// Approach: greedy, 
func getMaxLen(nums []int) int {
    
    prev_negative := -1
    prev_zero := -1
    negative_count := 0
    max_len := 0
    
    for i, num := range nums {
        if num < 0 {
            negative_count += 1
            if prev_negative == -1 {
                prev_negative = i
            }
        } else if num == 0 {
            prev_zero = i
            negative_count = 0
            prev_negative = -1
        }
        
        if negative_count % 2 == 0 {
            if i-prev_zero > max_len {
                max_len = (i-prev_zero)
            }
        } else {
            if i-prev_negative > max_len {
                max_len = (i-prev_negative)
            }
        }  
    }
    return max_len
}