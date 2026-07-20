class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = sorted(nums)
        new = []
        for i in s:
            if i not in new:
                new.append(i)

        if len(new) < 3:
            return new[-1]
        else:
            return new[-3]
