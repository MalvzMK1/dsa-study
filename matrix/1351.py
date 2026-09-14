class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        n = len(grid[0])
        count = 0
        for row in grid:
            i = n-1
            while row[i] < 0 and i >= 0:
                count += 1
                i -= 1
        return count

sol = Solution()
print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

        