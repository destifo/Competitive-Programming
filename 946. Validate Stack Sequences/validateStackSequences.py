class Solution:
    #did this one on first try by myself, amazing feeling. just treat pushed as a stack and popped as queue 
    def validateStackSequences(self, pushed, popped):
        i = 0
        while i < len(pushed):
            num = pushed[i]
            while num == popped[0]:
                pushed.pop(i)
                popped.pop(0)
                i -= 1
                if i < 0:
                    break
                num = pushed[i]
            i += 1

        if len(pushed) != 0 or len(popped) != 0:
            return False
        return True

sol = Solution()
isValid = sol.validateStackSequences([1,2,3,4,5], popped = [4,3,5,1,2])
print(isValid)