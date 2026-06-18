class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hmap = {}
        for i in range(len(numbers)):
            hmap[numbers[i]] = i
        for j in range(len(numbers)):
            x = target - numbers[j]
            if x in hmap and hmap[x] != j:
                return [j + 1, hmap[x] + 1]
        return []
