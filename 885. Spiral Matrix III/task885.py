class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        if R == 0 and C == 0:
            return []
        r, c = r0, c0
        spiral = [[r, c]]
        # direction_index: 0 - right, 1 - down, 2 - left, 3 - up
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0
        steps = 1
        while len(spiral) < R*C:
            # twice
            for _ in range(2):
                # make steps and then change a direction
                for _ in range(steps):
                    r += directions[direction_index][0]
                    c += directions[direction_index][1]
                    if 0 <= r < R and 0 <= c < C:
                        spiral.append([r, c])
                direction_index = (direction_index + 1) % 4
            steps += 1
        return spiral

# s = Solution()
# print(s.spiralMatrixIII(1,4,0,0))