class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] =1
        leftovers = 0
        pairs = 0
        for i in d.values():
            leftovers += i%2
            pairs += i//2
        return (pairs,leftovers)
        
                