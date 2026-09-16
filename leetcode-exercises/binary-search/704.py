class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return -1
        
sol = Solution()
print(sol.search([5], 5))
# print(sol.search([-1,0,3,5,9,12], 9))
# print(sol.search([-1,0,3,5,9,12], 2))