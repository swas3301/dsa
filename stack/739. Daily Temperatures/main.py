class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        st = []
        for i,j in enumerate(temperatures):
            while st and j > st[-1][0]:
                temp, index = st.pop()
                res[index] = (i - index)
            st.append([j,i])
        return res
