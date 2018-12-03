class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels_num = 0
        for i in S:
            if i in J: jewels_num += 1
        return jewels_num