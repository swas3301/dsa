class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a = set(allowed)

        res = len(words)
        for i in words:
            for j in i:
                if j not in allowed:
                    res = res - 1
                    break
        return res
