#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (61.29%)
# Likes:    445
# Dislikes: 0
# Total Accepted:    24.9K
# Total Submissions: 37.7K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 
# 现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
# left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
# 
# 求所能获得硬币的最大数量。
# 
# 说明:
# 
# 
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# 示例:
# 
# 输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        r = [[0] * (n + 2) for _ in range(n + 2)]
        v = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    r[i][j] = max(r[i][j], v[i] * v[k] * v[j] + r[i][k] + r[k][j])

        return r[0][n + 1]

# @lc code=end
