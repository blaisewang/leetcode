#
# @lc app=leetcode.cn id=1228 lang=python3
#
# [1228] 等差数列中缺失的数字
#
# https://leetcode-cn.com/problems/missing-number-in-arithmetic-progression/description/
#
# algorithms
# Easy (53.59%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 4.6K
# Testcase Example:  '[5,7,11,13]'
#
# 有一个数组，其中的值符合等差数列的数值规律，也就是说：
# 
# 
# 在 0 <= i < arr.length - 1 的前提下，arr[i+1] - arr[i] 的值都相等。
# 
# 
# 我们会从该数组中删除一个 既不是第一个 也 不是最后一个的值，得到一个新的数组  arr。
# 
# 给你这个缺值的数组 arr，请你帮忙找出被删除的那个数。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [5,7,11,13]
# 输出：9
# 解释：原来的数组是 [5,7,9,11,13]。
# 
# 
# 示例 2：
# 
# 输入：arr = [15,13,12]
# 输出：14
# 解释：原来的数组是 [15,14,13,12]。
# 
# 
# 
# 提示：
# 
# 
# 3 <= arr.length <= 1000
# 0 <= arr[i] <= 10^5
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)

# @lc code=end

