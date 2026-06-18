class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for i in emails:
            name, domain = i.split('@')
            name = name.split("+")[0]
            name = name.replace(".", "")
            unique.add((name, domain))
        return len(unique)
