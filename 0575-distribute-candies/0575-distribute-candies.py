class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        maxeat = n // 2
        diff = set(candyType)
        diffcount = len(diff)
        return min(diffcount , maxeat)