class Solution:
    def countCommas(self, n: int) -> int:
        total_count = 0
        i = 1_000
        j = 3

        while i <= n:
            total_count += (n - i) + 1
            j += 3
            i = 10 ** j

        return total_count


import time

print()
start = time.perf_counter()
result = Solution().countCommas(2_000_000)
end = time.perf_counter()
elapsed_time = end - start
print(f"Result: {result}\nTook {elapsed_time:.6f}")

