class Solution:
    
    # O(1) time,
    # O(1) space,
    # Approach: hashmap, 
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", 
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        
        date = date.split()
        ans = []
        ans.append(date[2])
        ans.append(months[date[1]])
        ans.append(("0" if len(date[0]) < 4 else "") + date[0][:-2])
        
        return "-".join(ans)