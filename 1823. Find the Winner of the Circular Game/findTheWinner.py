class Solution:
    # well, worked the first time
    def findTheWinner(self, n: int, k: int):
        ppl = []
        for i in range(1, n + 1):
            ppl.append(i)
        if n == 1:
            return 1
        game_round = 0
        cur_index = 0
        while len(ppl) > 1:
            game_round +=1
            cur_index = (cur_index + k - 1)%len(ppl)
            ppl.pop(cur_index)

        return ppl.pop()


sol = Solution()
print(sol.findTheWinner(5, 2))