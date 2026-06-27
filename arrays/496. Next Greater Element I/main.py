class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num : i for i, num in enumerate(nums1)}
        r = [-1] * len(nums1)
        s = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while s and cur > s[-1]:
                val = s.pop()
                idx = nums1Idx[val]
                r[idx] = cur
            if cur in nums1Idx:
                s.append(cur)
        return r
