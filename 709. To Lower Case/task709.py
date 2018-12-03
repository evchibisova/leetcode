class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new_str = ""
        for i in str:
            if 'A'<=i<='Z':
                new_str += chr(ord(i) + 32)
            else:
                new_str += i
        return new_str