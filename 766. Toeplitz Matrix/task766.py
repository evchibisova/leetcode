class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return None

        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

s = Solution()
print(s.isToeplitzMatrix([[1,1,3,4],
                            [5,1,2,3],
                            [9,5,1,2]]))