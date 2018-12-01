# https://leetcode.com/problems/di-string-match


class Solution(object):
    def di_string_match(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        A = [0]
        low, hi = 0, len(S)
        for i in S:
            if i == "I":
                low += 1
                A.append(low)
            else:
                hi -= 1
                A.append(hi)
        if low < 0:
            for i in range(len(A)):
                A[i] -= low

        return A


s = Solution()
print(s.di_string_match("IDID"))
print(s.di_string_match("III"))
print(s.di_string_match("DDI"))
