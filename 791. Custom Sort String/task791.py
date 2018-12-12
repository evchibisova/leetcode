class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # t_pointer point to sorted/unsorted boundary
        for i in S:
            T = T.replace(i, "") + i*T.count(i)
        return T

