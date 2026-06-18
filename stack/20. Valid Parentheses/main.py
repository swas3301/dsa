class Solution(object):
    def isValid(self, s):
        res = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                res.append(i)
            else:
                if not res:
                    return False
                top = res.pop()

                if i == ")" and top != "(":
                    return False
                if i == "}" and top != "{":
                    return False
                if i == "]" and top != "[":
                    return False
        return len(res)==0
