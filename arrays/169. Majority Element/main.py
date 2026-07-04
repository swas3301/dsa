class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxc = 0
        for num in nums:
            count[num] += 1
            if maxc < count[num]:
                res = num
                maxc = count[num]
        return res
