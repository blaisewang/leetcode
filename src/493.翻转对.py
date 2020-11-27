#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# https://leetcode-cn.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (29.73%)
# Likes:    148
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 28K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
# 
# 你需要返回给定数组中的重要翻转对的数量。
# 
# 示例 1:
# 
# 
# 输入: [1,3,2,3,1]
# 输出: 2
# 
# 
# 示例 2:
# 
# 
# 输入: [2,4,3,5,1]
# 输出: 3
# 
# 
# 注意:
# 
# 
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
# 
# 
#

# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        b, r = [], 0
        for n in reversed(nums):
            r += bisect_left(b, n)
            n2 = 2 * n
            i = bisect_left(b, n2)
            b.insert(i, n2)

        return r

# @lc code=end
