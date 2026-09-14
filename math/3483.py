class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        available_nums_amount = {}
        for d in digits:
            if d not in available_nums_amount:
                available_nums_amount[d] = 0
            available_nums_amount[d] += 1

        res = 0
        for i in range(100, 999, 2):
            used_nums = {}
            is_valid = True
            for d in str(i):
                d = int(d)
                if d not in available_nums_amount:
                    is_valid = False
                    break
                if d not in used_nums:
                    used_nums[d] = 0
                used_nums[d] += 1
                if used_nums[d] > available_nums_amount[d]:
                    is_valid = False
                    break
            if is_valid:
                res += 1

        return res

            


import time

print()

start = time.perf_counter()
result = Solution().totalNumbers([1,2,3,4])
end = time.perf_counter()
elapsed_time = end - start
print(f"Result: {result}\nTook {elapsed_time:.6f}")

