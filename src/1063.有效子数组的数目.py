#
# @lc app=leetcode.cn id=1063 lang=python3
#
# [1063] 有效子数组的数目
#
# https://leetcode-cn.com/problems/number-of-valid-subarrays/description/
#
# algorithms
# Hard (68.46%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 2K
# Testcase Example:  '[1,4,2,5,3]'
#
# 给定一个整数数组 A，返回满足下面条件的 非空、连续 子数组的数目：
# 
# 子数组中，最左侧的元素不大于其他元素。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,4,2,5,3]
# 输出：11
# 解释：有 11
# 个有效子数组，分别是：[1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3]
# 。
# 
# 
# 示例 2：
# 
# 输入：[3,2,1]
# 输出：3
# 解释：有 3 个有效子数组，分别是：[3],[2],[1] 。
# 
# 
# 示例 3：
# 
# 输入：[2,2,2]
# 输出：6
# 解释：有 6 个有效子数组，分别为是：[2],[2],[2],[2,2],[2,2],[2,2,2] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 50000
# 0 <= A[i] <= 100000
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        r = 0
        s = [(-float("inf"), len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            v = nums[i]
            while v <= s[-1][0]:
                s.pop()
            r += s[-1][1] - i
            s.append((v, i))

        return r

        
# @lc code=end

