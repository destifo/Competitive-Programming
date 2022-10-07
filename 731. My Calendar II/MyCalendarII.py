# O(mlogm) time, m--> number of calls
# O(m) space, 
# Approach: hastable, sorting
class MyCalendarTwo:

    def __init__(self):
        self.calendar = {} 

    def book(self, start: int, end: int) -> bool:
        self.calendar[start] = self.calendar.get(start, 0) + 1
        self.calendar[end] = self.calendar.get(end, 0) - 1
        
        srtd_calendar = sorted(self.calendar.keys())
        tot = 0
        for event in srtd_calendar:
            tot +=self.calendar[event]
            if tot > 2:
                self.calendar[start] -=1
                self.calendar[end] +=1
                return False
            
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)