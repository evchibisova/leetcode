# 


class Solution(object):
    def min_deletion_size(self, A):
        d_length = 0
        for l in zip(*A):
            if list(l) != sorted(l):
                d_length += 1

        return d_length


# a = ["cba","daf","ghi"]
# a = ["a","b"]
# a = ["zyx","wvu","tsr"]
# s = Solution()
# print(s.minDeletionSize(a))
