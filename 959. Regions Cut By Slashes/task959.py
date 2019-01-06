class Solution:
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        if not grid:
            return None
        

s = Solution()
print(s.regionsBySlashes(["\\/",
                         "/\\"]))