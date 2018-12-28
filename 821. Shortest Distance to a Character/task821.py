class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        if not S or not C:
            return None

        if C not in S:
            raise IndexError("Character not in string")

        # forward direction
        result = [0] * len(S)
        pos = S.find(C)
        for i in range(0, len(S)):
            if S[i] == C:
                pos = i
            result[i] = abs(i - pos)

        # opposite direction
        pos = S.rfind(C)
        for i in range(pos, -1, -1):
            if S[i] == C:
                pos = i
            result[i] = min(result[i], pos-i)

        return result
