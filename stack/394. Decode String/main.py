class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        st = []
        for i in range(len(s)):
            if s[i] != "]":
                st.append(s[i])
            else:
                str1 = ""
                while st[-1] != "[":
                    str1 = st.pop() + str1
                st.pop()

                k = ""
                while st and st[-1].isdigit():
                    k = st.pop() + k
                st.append(int(k) * str1)
        return "".join(st)
