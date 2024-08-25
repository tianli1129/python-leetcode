from typing import List

#solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in frequency:
                return True
            else:
                frequency[nums[i]] = 1
        return False

#test case
print(Solution().containsDuplicate([1,1,2,3]))