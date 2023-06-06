from collections import Counter, defaultdict

from matplotlib.pyplot import contour


class Solution:
    def groupAnagrams(self, strs):
        # naive solution
        n = len(strs)
        result = []

        counter_list = []
        for i in range(n):
            counter_list.append(Counter(strs[i]))

        visitedIndices = set()
        for i in range(n):
            if i in visitedIndices:
                continue
            result.append([strs[i]])
            for j in range(i + 1, n):
                if counter_list[i] == counter_list[j] and j not in visitedIndices:
                    visitedIndices.add(j)
                    result[len(result) - 1].append(strs[j])

        return result

    def groupAnagrams2(self, strs):
        # optimum one
        anagrams = defaultdict(list)
        
        for s in strs:
            count = Counter(s)
            anagram_key = ""
            for key in sorted(count):
                anagram_key += str(key)
                anagram_key += str(count[key])

            anagrams[anagram_key].append(s)

        return anagrams.values()

sol = Solution()
print(sol.groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))