class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        num = 0
        for word in words:
            match = True
            if len(pref) <= len(word):
                for i in range(0,len(pref)):
                    if pref[i] != word[i]:
                        match = False
                if match:
                    num = num + 1

        return num 
