class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        def help(nums):
            r1,r2 = 0,0
            for i in nums:
                temp = max(r1+i,r2)
                r1 = r2
                r2 = temp #  r2 hace the max value now 
            return r2
        c1 = help(nums[1:])
        c2 = help(nums[:-1])
        if c1 > c2:
            return c1
        else:
            return c2
