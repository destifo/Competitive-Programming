'''
https://leetcode.com/problems/find-good-days-to-rob-the-bank/
'''


class Solution:
    # naive solution 
    def goodDaysToRobBank(self, security, time):
        n = len(security)
        ans = []

        l = 0
        m, r = time, time + time
        while r < n:
            isGoodday = True
            for i in range(l, m):
                if security[i] < security[i + 1]:
                    isGoodday = False

            if isGoodday:
                for i in range(m, r):
                    if security[i] > security[i + 1]:
                        isGoodday = False

            if isGoodday:   ans.append(m)
            l +=1
            m, r = m + 1, r + 1

        return ans

    # optimum solution
    def goodDaysToRobBank2(self, security, time):
        n = len(security)
        nonincBeforei = [0] * n
        nondecAfteri = [0] * n
        ans = []

        for i in range(1, n):
            if security[i - 1] >= security[i]:
                nonincBeforei[i] = nonincBeforei[i - 1] + 1
            else:
                nonincBeforei[i] = nonincBeforei[i - 1]

        for i in range(n-2, -1, -1):
            if security[i] <= security[i + 1]:
                nondecAfteri[i] = nondecAfteri[i + 1] + 1
            else:
                nondecAfteri[i] = nondecAfteri[i + 1]

        for i in range(time, n - time):
            if nonincBeforei[i] - nonincBeforei[i - time] == time and nondecAfteri[i] - nondecAfteri[i + time] == time:
                ans.append(i)

        return ans

sol = Solution()
print(sol.goodDaysToRobBank2([5,3,3,3,5,6,2],2))