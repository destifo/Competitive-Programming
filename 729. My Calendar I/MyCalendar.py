from collections import deque


class MyCalendar:

    def __init__(self):
        self.calendar = {}
        
    # O(n^2) time,
    # O(n) space,
    # Approach: hashmap, sorting
    def book(self, start: int, end: int) -> bool:
        calendar = self.calendar
        if start not in calendar.keys():
            calendar[start] = 0
        if end not in calendar.keys():
            calendar[end] = 0
        calendar[start] += 1
        calendar[end] -=1
        
        sorted_date = sorted(calendar.keys())
        
        tot = 0
        for day in sorted_date:
            tot +=calendar[day]
            if tot > 1:
                calendar[start] -=1
                calendar[end] +=1
                return False
        
        return True    


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))