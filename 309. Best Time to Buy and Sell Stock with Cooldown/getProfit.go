package maxProfit;


import "math";


type State struct {
    index int
    buying bool
}


func getProfit(index int, buying bool, prices *[]int, memo *map[State]int) int {
    
    if index >= len(*prices) {
        return 0;
    }
    
    state := State{index, buying};
    if _, found := (*memo)[state]; found {
        return (*memo)[state];
    }
    
    best_opt := 0;
    if buying {
        buy := getProfit(index+1, !buying, prices, memo) - (*prices)[index];
        skip_buy := getProfit(index+1, buying, prices, memo);
        best_opt = int(math.Max(float64(buy), float64(skip_buy)));
    } else {
        sell := getProfit(index+2, !buying, prices, memo) + (*prices)[index];
        skip_sell := getProfit(index+1, buying, prices, memo);
        best_opt = int(math.Max(float64(sell), float64(skip_sell)));
    }
    
    (*memo)[state] = best_opt;
    return best_opt;
}


func maxProfit(prices []int) int {
    memo := make(map[State]int);
    return getProfit(0, true, &prices, &memo);
}


// O(n) time,
// O(n) space,
// Approach: dp tabulation, bottom up
func maxProfit2(prices []int) int {
    dp := make([][]int, len(prices)+2);
    for i := 0; i <= len(prices)+1; i++ {
        dp[i] = make([]int, 2);
    }
    
    for i:= len(prices)-1; i >= 0; i-- {
        buy := dp[i+1][1] - prices[i];
        skip_buy := dp[i+1][0];
        dp[i][0] = int(math.Max(float64(buy), float64(skip_buy)));
        sell := dp[i+2][0] + prices[i];
        skip_sell := dp[i+1][1];
        dp[i][1] = int(math.Max(float64(sell), float64(skip_sell)));
    }
    return dp[0][0];
}