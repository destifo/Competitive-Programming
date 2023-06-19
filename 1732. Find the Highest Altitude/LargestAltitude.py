from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: array,
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        max_altitude = 0

        for change in gain:
            height += change
            max_altitude = max(max_altitude, height)

        return max_altitude
