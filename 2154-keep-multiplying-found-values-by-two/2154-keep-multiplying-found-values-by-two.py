class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while True:
            if_found = False
            for num in nums:
                if num == original:
                    original *= 2
                    if_found = True
                    break
            if if_found == False:
                break
        return original
        