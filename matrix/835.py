class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        img1_pairs, img2_pairs = [], []

        i, j = 0, 0
        n, m = len(img1), len(img1[0])
        while i < n:
            while j < m:
                if img1[i][j] == 1:
                    img1_pairs.append((i, j))
                if img2[i][j] == 1:
                    img2_pairs.append((i, j))
                j += 1
            i += 1
            j = 0

        counts = {}

        for p1 in img1_pairs:
            for p2 in img2_pairs:
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]
                if (dx, dy) not in counts:
                    counts[(dx, dy)] = 0
                counts[(dx, dy)] += 1

        biggest = 0

        for pair in counts:
            if counts[pair] > biggest:
                biggest = counts[pair]

        return biggest



sol = Solution()
m = [[0,0,0],[1,0,0],[1,0,0]] 
n = [[0,0,1],[0,0,1],[0,0,0]] 
print(sol.largestOverlap(m, n))
