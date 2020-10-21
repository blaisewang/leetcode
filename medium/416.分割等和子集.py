#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (48.88%)
# Likes:    437
# Dislikes: 0
# Total Accepted:    60.3K
# Total Submissions: 121.8K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s, f = 0, 1
        for i in nums:
            s += i
            f = f | f << i

        if s % 2 == 0:
            s //= 2
        else:
            return False

        if (1 << s) & f != 0:
            return True
        else:
            return False

# @lc code=end
