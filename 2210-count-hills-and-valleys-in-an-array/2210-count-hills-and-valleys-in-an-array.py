class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        new = [nums[0]]
        for i in nums:
            if new[-1] != i:
                new.append(i)
        count = 0
        for i in range(1 , len(new)-1):
            if new[i-1] < new[i] >new[i+1]:
                count +=1
            elif new[i-1] > new[i] < new[i+1]:
                count +=1
        return count