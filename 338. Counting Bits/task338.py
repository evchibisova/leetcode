class Solution(object):
    def count_bits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        answer = [0]
        n = 1
        for i in range(1, num+1):
            if i >= 2*n:
                n *= 2
            answer.append(answer[i - n] + 1)
        return answer

s = Solution()
print(s.count_bits(2))
print(s.count_bits(5))