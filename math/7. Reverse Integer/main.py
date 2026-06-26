class Solution:
    def reverse(self, x: int) -> int:
        minr = -(2**31)
        maxr = (2**31) - 1

        res = 0
        n = abs(x)
        while n > 0:
            last = n%10
            res = (res * 10) + last
            n = n // 10

        if res < minr or res > maxr:
            return 0
        if x < 0:
            res = -res
            return res
        else:
            return res
