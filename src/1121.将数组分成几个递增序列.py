#
# @lc app=leetcode.cn id=1121 lang=python3
#
# [1121] 将数组分成几个递增序列
#
# https://leetcode-cn.com/problems/divide-array-into-increasing-sequences/description/
#
# algorithms
# Hard (54.77%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    907
# Total Submissions: 1.7K
# Testcase Example:  '[1,2,2,3,3,4,4]\n3'
#
# 给你一个 非递减 的正整数数组 nums 和整数 K，判断该数组是否可以被分成一个或几个 长度至少 为 K 的 不相交的递增子序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,2,3,3,4,4], K = 3
# 输出：true
# 解释：
# 该数组可以分成两个子序列 [1,2,3,4] 和 [2,3,4]，每个子序列的长度都至少是 3。
# 
# 
# 示例 2：
# 
# 输入：nums = [5,6,6,7,8], K = 3
# 输出：false
# 解释：
# 没有办法根据条件来划分数组。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= K <= nums.length
# 1 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        c = Counter(nums)
        mc = max(c.values())
        return K * mc <= len(nums)

# @lc code=end
