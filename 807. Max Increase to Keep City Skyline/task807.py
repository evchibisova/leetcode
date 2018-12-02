class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        total_sum = 0

        column_highs = []
        for column in range(len(grid[0])):
            max_in_column = 0
            for row in grid:
                if max_in_column < row[column]:
                    max_in_column = row[column]
            column_highs.append(max_in_column)

        for row in grid:
            max_in_row = max(row)
            for building_num in range(len(row)):
                total_sum += min(max_in_row, column_highs[building_num]) - row[building_num]

        return total_sum


# s = Solution()
# grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# print(s.maxIncreaseKeepingSkyline(grid))