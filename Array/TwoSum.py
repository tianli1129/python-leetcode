
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}
        n = len(nums)
        for i in range(n):
            complement = target-nums[i]
            if complement in mappings:
                return {mappings[complement],i}
            else:
                mappings[nums[i]] = i
        return []

print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))
