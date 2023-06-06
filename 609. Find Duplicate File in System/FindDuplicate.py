'''
https://leetcode.com/problems/find-duplicate-file-in-system/
'''


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_path =  dict()
        result = []
        
        for path in paths:
            path = path.split()
            dir = path[0]
            m = len(path)
            for i in range(1, m):
                file = path[i]
                _file = file.split('(')
                content = _file[1]
                content = content[:-1]
                dir_path = dir + '/' + _file[0]
                if content not in content_path.keys():
                    content_path[content] = []
                content_path[content].append(dir_path)
                
        for lst in content_path.values():
            if len(lst) > 1:
                result.append(lst)
                
        return result