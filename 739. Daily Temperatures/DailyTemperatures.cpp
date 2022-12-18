class Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: mono stack,
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> stack(0, 0);
        vector<int> answer(n, 0);
        
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && temperatures[i] > temperatures[stack.back()]) {
                int popped = stack.back();
                stack.pop_back();
                answer[popped] = i-popped;
            }  
            stack.push_back(i);
        }
        
        return answer;
    }
};