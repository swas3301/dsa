class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0,1,1]
        if n < 3:
            return a[n]

        for i in range(3,n+1):
            a[0],a[1],a[2] = a[1], a[2], sum(a)
        return a[2]
