// O(n) time,
// O(n) space,
// Approach: mono stack, 
func dailyTemperatures(temperatures []int) []int {
    var n int = len(temperatures);
    answer:= make([]int, n);
    var stack []int;
    
    for i:= 0; i < n; i++ {
        for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]] {
            popped:= stack[len(stack)-1];
            stack = stack[:len(stack)-1];
            answer[popped] = i-popped;
        }
        stack = append(stack, i);
    }
    
    return answer;
}