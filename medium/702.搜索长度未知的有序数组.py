#
# @lc app=leetcode.cn id=702 lang=python3
#
# [702] 搜索长度未知的有序数组
#
# https://leetcode-cn.com/problems/search-in-a-sorted-array-of-unknown-size/description/
#
# algorithms
# Medium (69.89%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 3.2K
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# 给定一个升序整数数组，写一个函数搜索 nums 中数字 target。如果 target 存在，返回它的下标，否则返回
# -1。注意，这个数组的大小是未知的。你只可以通过 ArrayReader 接口访问这个数组，ArrayReader.get(k) 返回数组中第 k
# 个元素（下标从 0 开始）。
# 
# 你可以认为数组中所有的整数都小于 10000。如果你访问数组越界，ArrayReader.get 会返回 2147483647。
# 
# 
# 
# 样例 1：
# 
# 输入: array = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 存在在 nums 中，下标为 4
# 
# 
# 样例 2：
# 
# 输入: array = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不在数组中所以返回 -1
# 
# 
# 
# 注释 ：
# 
# 
# 你可以认为数组中所有元素的值互不相同。
# 数组元素的值域是 [-9999, 9999]。
# 
# 
#

# @lc code=start
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
    def get(self, index: int) -> int:
        pass


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        if reader.get(0) == target:
            return 0

        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1

        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)

            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1

# @lc code=end
