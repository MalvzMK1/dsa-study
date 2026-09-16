class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}

        for s in strs:
            srt = str(sorted(s))
            res[srt] = [s] + res.get(srt, [])
        
        ans = []

        for c in res:
            ans.append(res[c])
        
        return ans

sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))