class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        num = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if num > 0:
                    num = num - 1
            else:
                num = num+1
        return num
