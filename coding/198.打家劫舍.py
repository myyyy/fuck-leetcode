#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in nums]
        dp[0] = nums[0]
        l = len(nums)
        for i in range(1,l-1):
            print dp[i-1],nums[i+1],nums[i]
            dp[i+1] =max(dp[i-1]+nums[i+1],nums[i])
            dp[i]
        print dp
        return dp[-1]
# @lc code=end

