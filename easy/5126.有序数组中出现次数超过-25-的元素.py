#
# @lc app=leetcode.cn id=5126 lang=python3
#
# [5126] 有序数组中出现次数超过25%的元素
#
# https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#
# algorithms
# Easy (60.78%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    6.9K
# Total Submissions: 11.2K
# Testcase Example:  '[1,2,2,6,6,6,6,7,10]'
#
# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
# 
# 请你找到并返回这个整数
# 
# 
# 
# 示例：
# 
# 
# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 4:
            return arr[0]
        for i in range(n // 4 * 3 + 1):
            if arr[i] == arr[i + n // 4]:
                return arr[i]

# @lc code=end
