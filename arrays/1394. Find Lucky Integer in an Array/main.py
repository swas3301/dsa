class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        for i in arr:
            count = 0 
            for j in arr:
                if i == j:
                    count += 1
            if count == i:
                if count > res:
                    res = count
        return res
