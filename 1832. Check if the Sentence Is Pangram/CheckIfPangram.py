class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: hashset, hashtable
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26