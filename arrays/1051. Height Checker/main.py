class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct = sorted(heights)
        c = 0 
        for i in range(len(heights)):
            if heights[i] != correct[i]:
                c = c + 1
        return c
