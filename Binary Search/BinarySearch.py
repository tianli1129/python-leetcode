from typing import List

#solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target<nums[m]:
                r = m-1
            else:
                l = m+1
        return -1

#testcase
print(Solution().search([-1,0,3,5,9,12],9))