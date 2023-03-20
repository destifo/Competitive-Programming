class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, 
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = float('inf')
        early_hour = len(customers)
        
        y_count_right = []
        tot = 0
        for i in range(len(customers)-1, -1, -1):
            y_count_right.append(tot)
            tot += 1 if customers[i] == "Y" else 0
            
        y_count_right.append(tot)
        y_count_right.reverse()
        
        tot = 0
        for i in range(len(customers)):
            curr_penalty = tot + y_count_right[i]
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                early_hour = i
                
            tot += 1 if customers[i] == "N" else 0
            
        if tot < min_penalty:
            early_hour = len(customers)
            
        return early_hour