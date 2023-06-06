from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: sorting, greedy
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        '''
        our goal is to maximize our score, so we can be greedy
        and choose the label with the highest value till we
        exhaust it or reach useLimit, then we go to the next
        highest, we go on this manner till we get numWanted amount of labels or we use all our labels
        '''
        
        # create map of labels with value == useLimit
        label_usage = defaultdict(int)
        for label in labels:
            label_usage[label] = useLimit
        
        # group labels with their values, and sort in dec order
        label_value = sorted([(values[i], labels[i]) for i in range(len(labels))], reverse=True)
                
        # init score and go over the labels
        score = 0
        size = 0
        for value, label in label_value:
            if size == numWanted:    break
            if label_usage[label] <= 0:
                continue
                
            label_usage[label] -= 1
            score += value
            size += 1
        
        # return max score
        return score