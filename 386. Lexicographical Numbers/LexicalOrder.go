// O(n) time,
// O(1) space, space used only for the answer
// Approach: math,
func lexicalOrder(n int) []int {
    
    answer:= make([]int, 0);
    answer = append(answer, 1);
    num := 1;
    
    for i:= 1; i < n; i++ {
        if num * 10 <= n {
            num *= 10;
        } else if num+1 <= n && num % 10 != 9 {
            num += 1;
        } else {
            for (num/10) % 10 == 9 {
                num /= 10;
            }
            num = num/10 + 1;
        }
        answer = append(answer, num);
    }
    return answer;    
}