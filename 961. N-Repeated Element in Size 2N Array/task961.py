class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        numbers_set = set()
        for i in A:
            if i in numbers_set:
                return i
                break
            else:
                numbers_set.add(i)