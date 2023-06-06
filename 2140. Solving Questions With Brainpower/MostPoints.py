'''
https://leetcode.com/problems/solving-questions-with-brainpower/
'''

class Solution:
    def mostPoints(self, questions):
        # naive approach
        n = len(questions)
        def maxScore(i, score):
            if i >= n:
                return score

            return max(maxScore(i + questions[i][1] + 1, score + questions[i][0]), maxScore(i + 1, score))

        return maxScore(0, 0)


    def mostPoints2(self, questions):
        # fast solution, had to dig deep for it and with help too
        n = len(questions)
        maxAtIndex = {}
        maxAtIndex[n - 1] = questions[n - 1][0]
        score = 0
        inbound_indices = []
        for i in range(n - 2, -1, -1):
            question = questions[i]
            if (question[1] + i + 1) >= n:
                maxAtIndex[i] = max(question[0], maxAtIndex.get(i + 1, 0))
                score = max(score, maxAtIndex[i])
            else:
                maxAtIndex[i] = max(maxAtIndex[i + 1], maxAtIndex[i + questions[i][1] + 1] + questions[i][0])
            score = max(score, maxAtIndex[i])

        # for i in inbound_indices:
        #     print(i)
        #     maxAtIndex[i] = max(maxAtIndex[i + 1], maxAtIndex[i + questions[i][1] + 1] + questions[i][0])
        #     score = max(score, maxAtIndex[i])

        return score

sol = Solution()
print(sol.mostPoints2([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]
))