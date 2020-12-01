#
# @lc app=leetcode.cn id=1538 lang=python3
#
# [1538] 找出隐藏数组中出现次数最多的元素
#
# https://leetcode-cn.com/problems/guess-the-majority-in-a-hidden-array/description/
#
# algorithms
# Medium (51.96%)
# Likes:    3
# Dislikes: 0
# Total Accepted:    53
# Total Submissions: 102
# Testcase Example:  '[0,0,1,0,1,1,1,1]'
#
# 给定一个整数数组 nums，且 nums 中的所有整数都为 0 或 1。你不能直接访问这个数组，你需要使用 API ArrayReader ，该 API
# 含有下列成员函数：
# 
# 
# int query(int a, int b, int c, int d)：其中 0 <= a < b < c < d <
# ArrayReader.length() 。此函数查询以这四个参数为下标的元素并返回：
# 
# 
# 4 : 当这四个元素相同（0 或 1）时。
# 2 : 当其中三个元素的值等于 0 且一个元素等于 1 时，或当其中三个元素的值等于 1 且一个元素等于 0 时。
# 0 : 当其中两个元素等于 0 且两个元素等于 1 时。
# 
# 
# int length()：返回数组的长度。
# 
# 
# 你可以调用 query() 最多 2 * n 次，其中 n 等于 ArrayReader.length()。
# 
# 返回 nums 中出现次数最多的值的任意索引，若所有的值出现次数均相同，返回 -1。
# 
# 进阶：要找到出现次数最多的元素，需要至少调用 query() 多少次？
# 
# 
# 
# 示例 1：
# 
# 输入: nums = [0,0,1,0,1,1,1,1]
# 输出: 5
# 解释: API 的调用情况如下：
# reader.length() // 返回 8，因为隐藏数组中有 8 个元素。
# reader.query(0,1,2,3) // 返回 2，查询元素 nums[0], nums[1], nums[2], nums[3] 间的比较。
# // 三个元素等于 0 且一个元素等于 1 或出现相反情况。
# reader.query(4,5,6,7) // 返回 4，因为 nums[4], nums[5], nums[6], nums[7] 有相同值。
# 我们可以推断，最常出现的值在最后 4 个元素中。
# 索引 2, 4, 6, 7 也是正确答案。
# 
# 
# 示例 2:
# 
# 输入: nums = [0,0,1,1,0]
# 输出: 0
# 
# 
# 示例 3:
# 
# 输入: nums = [1,0,1,0,1,0,1,0]
# 输出: -1
# 
# 
# 
# 
# 提示:
# 
# 
# 5 <= nums.length <= 10^5
# 0 <= nums[i] <= 1
# 
# 
#

# @lc code=start
# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        x = reader.query(0, 1, 2, 3)
        if not x:
            start = 5
            more = 1
            if reader.query(1, 2, 3, 4):
                b, c = 4, 0
                a = 2 if reader.query(0, 2, 3, 4) else 1
            else:
                a, b = 0, 4
                c = 1 if reader.query(0, 2, 3, 4) else 2
        elif x == 2:
            start = 5
            x = reader.query(1, 2, 3, 4)
            if not x:
                more = 1
                a, c = 0, 4
                if reader.query(0, 2, 3, 4):
                    b = 2
                else:
                    b = 1
            elif x == 2:
                x = reader.query(0, 2, 3, 4)
                if not x:
                    more = 1
                    a, b, c = 1, 2, 0
                elif x == 2:
                    more = 3
                    a, b = 0, 1
                    c = 2 if reader.query(0, 1, 3, 4) == 4 else 3
                else:
                    more = 3
                    a, b, c = 0, 2, 1
            else:
                more = 3
                a, b, c = 1, 2, 0
        else:
            a, b = 0, 1
            for i in range(4, n - 1, 2):
                x = reader.query(0, 1, i, i + 1)
                if not x:
                    start = i + 2
                    more = i - 2
                    c = i
                    break
                elif x == 2:
                    start = i + 2
                    more = i
                    c = i if reader.query(0, 1, 2, i) == 2 else i + 1
                    break
            else:
                return 0

        for i in range(start, n - 1, 2):
            more += reader.query(a, b, i, i + 1) - 2

        if n - start & 1:
            x = [a, b, c]
            x.sort()
            more += reader.query(*x, n - 1) - 1

        if more > 0:
            return a
        elif not more:
            return -1
        else:
            return c

# @lc code=end
