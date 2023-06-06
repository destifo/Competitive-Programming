package maxJump


func goForward(index int, stones *[]int, max_jump *int) {
    if index+2 < len(*stones) {
        curr_jump := (*stones)[index+2]-(*stones)[index]
        if curr_jump > *max_jump {
            *max_jump = curr_jump
        }
        goForward(index+2, stones, max_jump)
    } else if index+1 < len(*stones) {
        curr_jump := (*stones)[index+1] - (*stones)[index]
        if curr_jump > *max_jump {
            *max_jump = curr_jump
        }
        goForward(index+1, stones, max_jump)
    }
}


func goBackward(index int, stones *[]int, max_jump *int) {
    if index-2 >= 0 {
        curr_jump := (*stones)[index] - (*stones)[index-2]
        // if index == 3 {
        //     fmt.Printf("%d", curr_jump)
        // }
        if curr_jump > *max_jump {
            *max_jump = curr_jump
        }
        goBackward(index-2, stones, max_jump)
    } else if index-1 >= 0 {
        curr_jump := (*stones)[index] - (*stones)[index-1]
        if curr_jump > *max_jump {
            *max_jump = curr_jump
        }
        goBackward(index-1, stones, max_jump)
    }
}


// O(n) time,
// O(1) space,
// Approach: greedy, 
func maxJump(stones []int) int {
    max_jump := 0
    goForward(0, &stones, &max_jump)
    last_pos := len(stones)-2
    if len(stones)%2 == 0 {
        last_pos = len(stones)-3
    }
    
    if last_pos >= 0 && (stones[len(stones)-1]-stones[last_pos]) > max_jump {
        max_jump = stones[len(stones)-1] - stones[last_pos]
    }
    goBackward(last_pos, &stones, &max_jump)
    return max_jump
}