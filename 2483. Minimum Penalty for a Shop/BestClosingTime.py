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
    
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, array, one pass
    def bestClosingTime2(self, customers: str) -> int:
        min_pen = 0
        curr_pen = 0
        ans = 0
        for i, status in enumerate(customers):
            if status == "Y":
                curr_pen -= 1
            else:
                curr_pen += 1
            if curr_pen < min_pen:
                ans = i+1
                min_pen = curr_pen
            
        return ans