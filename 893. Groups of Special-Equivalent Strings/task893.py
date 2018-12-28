class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        s = set()
        for i in A:
            s.add("".join(sorted(i[::2])) + "".join(sorted(i[1::2])))
        return len(s)
