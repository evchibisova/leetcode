class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_n = bin(N)[2:]

        distance = 0
        last_one = 0
        for i in range(len(bin_n)):
            if bin_n[i] == "1":
                distance = max(distance, i-last_one)
                last_one = i

        return distance
