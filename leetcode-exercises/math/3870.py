import math

class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1_000:
            return 0

        levels = self.extractLevels(n) # multiplier is according to level
        if levels == 1:
            return n - 1000 + 1

        i = n
        multiplier = 1
        total_count = 0

        while i > 1_000:
            total_count += (i % 1000 + 1) * multiplier
            i //= 1_000
            multiplier += 1

        return total_count 
        
    def extractLevels(self, n: int) -> int:
        return math.ceil(len(str(n)) / 3) - 1


sol = Solution()
print(sol.countCommas(2019))
# print(math.ceil(len(str(1000)) / 3) - 1)