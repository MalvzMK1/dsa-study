import math

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        target_ord, n = ord(target), len(letters)

        if ord(letters[n-1]) <= target_ord:
            return letters[0]

        l, r = 0, n
        mid = 0
        smallest_difference: tuple[str, int] = ('Z', math.inf)

        while l < r:
            mid = (l + r) // 2
            letter_ord = ord(letters[mid])

            if letter_ord <= target_ord:
                l = mid + 1
            else:
                difference =  letter_ord - target_ord
                if difference < smallest_difference[1]:
                    smallest_difference = (letters[mid], difference)
                r = mid

        return smallest_difference[0]

sol = Solution()
print(sol.nextGreatestLetter(["c","f","j"], 'a'))