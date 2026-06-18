class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        history = {}

        for i, num in enumerate(nums):
            if num in history and i - history[num] <=k:
                return True
            
            history[num]=i
                    
        return False
