'''
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
'''


from collections import Counter


class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        task_count = Counter(tasks)
        rounds = 0
        
        for value in task_count.values():
            if value < 2:
                return -1
                
            qutnt = value // 3
            mod = value % 3
            if mod == 1:
                qutnt -=1
                mod += 3
            rounds +=qutnt
            
            qutnt = mod // 2
            rounds +=qutnt
            
        return rounds


sol = Solution()
print(sol.minimumRounds([66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]))