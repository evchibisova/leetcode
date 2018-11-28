class Solution(object):
    def min_deletion_size2(self, A):
        d_length = 0
        for i in range(len(A[0])):
            for j in range(len(A) - 1):
                if A[j + 1][i] < A[j][i]:
                    d_length += 1
                    break


a = ["cba","daf","ghi"]
a = ["a","b"]
a = ["zyx","wvu","tsr"]
s = Solution()
print(s.minDeletionSize(a))