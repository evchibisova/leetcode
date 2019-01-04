class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A, B = A.split(), B.split()

        d = dict()
        for lst in (A, B):
            for i in lst:
                if i not in d:
                    d[i] = 0
                d[i] += 1
        return [i for i in d if d[i] == 1]