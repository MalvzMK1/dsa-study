from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[list[str]]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return res.values()

sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))