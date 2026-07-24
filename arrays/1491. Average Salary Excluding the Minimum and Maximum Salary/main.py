class Solution:
    def average(self, salary: List[int]) -> float:
        s = sorted(salary)
        s.pop(-1)
        s.pop(0)
        return sum(s) / len(s)
