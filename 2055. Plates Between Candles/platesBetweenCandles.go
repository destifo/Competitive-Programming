
// O(len(s) + len(queries)) time,
// O(len(s) + len(queries)) space,
// Approach: prefix sum, 
func platesBetweenCandles(s string, queries [][]int) []int {
    size := len(s);
    prefix_sum := make([]int, size);
    next_candle_right := make([]int, size);
    next_candle_left := make([]int, size);
    
    plates := 0;
    next_candle := -1;
    for i, item := range s {
        prefix_sum[i] = plates;
        if item == '*' {
            plates += 1;
        } else {
            next_candle = i;
        }
        next_candle_left[i] = next_candle;
    }
    
    s_char := []rune(s);
    next_candle = -1;
    for i := len(s)-1; i >= 0; i-- {
        if s_char[i] == '|' {
            next_candle = i;
        }
        next_candle_right[i] = next_candle;
    }
    
    answer := make([]int, len(queries));
    
    for i, query := range queries {
        start := query[0];
        end := query[1];
        left_candle := next_candle_right[start];
        right_candle := next_candle_left[end];
        
        if left_candle == -1 || left_candle >= end {
            continue;
        }
        
        if right_candle == -1 || right_candle <= start {
            continue;
        }
        
        answer[i] = prefix_sum[right_candle] - prefix_sum[left_candle];
    }
    
    return answer;
}