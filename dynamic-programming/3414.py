import math
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        if len(intervals) < 2:
            return 0
        
        intervals_with_idx = sorted(
            [(r, l, weight, i) for i, (l, r, weight) in enumerate(intervals)]
        )

        dp = [[None, None, None, None] for i in intervals_with_idx]

        for i, (_, _, weight, idx) in enumerate(intervals_with_idx):
            p = self.get_last_compatible(i, intervals_with_idx)
            for k in range(0, 4):
                best = dp[i-1][k] if i > 0 else (0, [])
                if i == 0:
                    cand = (weight, [idx])
                    best = self.get_better(best, cand)
                elif p != -1 and dp[p][k-1] is not None:
                    new_score = dp[p][k-1][0] + weight
                    new_idxs = sorted(dp[p][k-1][1] + [idx])
                    cand = (new_score, new_idxs)
                    best = self.get_better(best, cand)
                dp[i][k] = best

        return dp

    def get_last_compatible(self, i: int, arr: list[tuple[int, int, int, int]]) -> int:
        ends = [item[0] for item in arr]
        return bisect_left(ends, arr[i][1]) - 1


    def get_better(self, x: tuple[int, list[int]], y: tuple[int, list[int]]) -> tuple[int, list[int]]:
        if x[0] > y[0]:
            return x
        if y[0] > x[0]:
            return y

        return self.get_lexicographic_smallest(x, y)

    def get_lexicographic_smallest(self, x: tuple[int, list[int]], y: tuple[int, list[int]]) -> tuple[int, list[int]]:
        i = 0
        x_len, y_len = len(x[1]), len(y[1])

        if x_len < y_len:
            return x
        if y_len < x_len:
            return y

        while i < max(x_len, y_len):
            if x[1][i] < y[1][i]:
                return x
            elif x[1][i] > y[1][i]:
                return y

        
sol = Solution()
print(sol.maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]))