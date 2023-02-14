class Solution:
    
    # O(len(s)) time,
    # O(len(s)) space,
    # Approach: prefix sum, greedy, string
    def minimumDeletions(self, s: str) -> int:
        a_at = []
        a_count = 0
        
        for ch in s:
            a_at.append(a_count)
            if ch == "a":
                a_count += 1

        b_count = len(s) - a_count
        min_deletion = min(b_count, a_count)
        for index in range(len(s)):
            before_index_b_count = index - a_at[index]
            from_index_a_count = a_count - a_at[index]
            curr_deletion = before_index_b_count + from_index_a_count
            min_deletion = min(min_deletion, curr_deletion)
        
        return min_deletion