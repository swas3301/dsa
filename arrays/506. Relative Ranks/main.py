class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse=True)
        d = {}
        for i in range(len(s)):
            if i == 0:
                d[s[i]] = "Gold Medal"
            elif i == 1:
                d[s[i]] = "Silver Medal"
            elif i == 2:
                d[s[i]] = "Bronze Medal"
            else:
                d[s[i]] = str(i + 1)
        a = []
        for i in score:
            a.append(d[i])
        return a
