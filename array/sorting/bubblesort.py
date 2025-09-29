def bubble(nums):
    n = len(nums)

    for _ in nums:
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

arr = [5, 4, 3, 2, 1]

bubble(arr)

print(arr)

