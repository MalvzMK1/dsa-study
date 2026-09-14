class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        mid = 0

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return mid+1 if nums[mid] < target else mid

sol = Solution()
print(sol.searchInsert([1,3,5,6], 0))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 7))
print(sol.searchInsert([1,3], 0))