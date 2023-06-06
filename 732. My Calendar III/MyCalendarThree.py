class MyCalendarThree:

    def __init__(self):
        self.calendar = {}
        
    # O((nlogn)^2) time, n --> no of calls to book, or size of our stream
    # O(n) space,  
    # Approach: hashmap, sorting
    def book(self, start: int, end: int) -> int:
        calendar = self.calendar
        calendar[start] = calendar.get(start, 0) + 1
        calendar[end] = calendar.get(end, 0) - 1
        k = 0
        
        srtd_cal = sorted(calendar.keys())
        tot = 0
        for day in srtd_cal:
            tot += calendar[day]
            k = max(k, tot)
            
        return k
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)