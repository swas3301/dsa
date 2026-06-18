class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = -1
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                a = 3*num[i]
                
                if int(a) > int(s):
                    s = a
        if int(s)>-1:
            return s
        else:
            return ""
