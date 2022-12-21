package maxProfit;


import "math";


type State struct {
    index int
    buying bool
    rem int
}


func make_transaction(index int, buying bool, rem int, prices *[]int, memo *map[State]int) int {
    
    if index == len(*prices) || rem == 0 {
        return 0;
    }
    
    curr_state := State{index, buying, rem};
    ans, ok := (*memo)[curr_state];
    if ok {
        return ans;
    }
    
    var answer int;
    if buying {
        buy := make_transaction(index+1, !buying, rem, prices, memo) - (*prices)[index];
        skip_buy := make_transaction(index+1, buying, rem, prices, memo);
        answer = int(math.Max(float64(buy), float64(skip_buy)));
    } else {
        sell := make_transaction(index+1, !buying, rem-1, prices, memo) + (*prices)[index];
        skip_sell := make_transaction(index+1, buying, rem, prices, memo);
        answer = int(math.Max(float64(sell), float64(skip_sell)));
    }
    
    (*memo)[curr_state] = answer;
    return answer;
}


// O(n) time,
// O(n) space,
// Approach: dp, top down, memoization, 
func maxProfit(prices []int) int {
    memo := make(map[State]int);
    return make_transaction(0, true, 2, &prices, &memo);
}