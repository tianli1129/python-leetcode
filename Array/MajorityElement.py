from typing import List

#solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

#test case
print(Solution().majorityElement([1,1,1,2,2]))
        