#
# @lc app=leetcode.cn id=1428 lang=python3
#
# [1428] 至少有一个 1 的最左端列
#
# https://leetcode-cn.com/problems/leftmost-column-with-at-least-a-one/description/
#
# algorithms
# Medium (60.53%)
# Likes:    8
# Dislikes: 0
# Total Accepted:    300
# Total Submissions: 488
# Testcase Example:  '[[0,0],[1,1]]'
#
# （这是一个交互题）
# 
# 我们称只包含元素 0 或 1 的矩阵为二进制矩阵。矩阵中每个单独的行都按非递减顺序排序。
# 
# 给定一个这样的二进制矩阵，返回至少包含一个 1 的最左端列的索引（从 0 开始）。如果这样的列不存在，返回 -1。
# 
# 您不能直接访问该二进制矩阵。你只可以通过 BinaryMatrix 接口来访问。
# 
# 
# BinaryMatrix.get(row, col) 返回位于索引 (row, col) （从 0 开始）的元素。
# BinaryMatrix.dimensions() 返回含有 2 个元素的列表 [rows, cols]，表示这是一个 rows * cols的矩阵。
# 
# 
# 如果提交的答案调用 BinaryMatrix.get 超过 1000 次，则该答案会被判定为错误答案。提交任何试图规避判定机制的答案将会被取消资格。
# 
# 下列示例中， mat 为给定的二进制矩阵。您不能直接访问该矩阵。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: mat = [[0,0],[1,1]]
# 输出: 0
# 
# 
# 示例 2:
# 
# 
# 
# 
# 输入: mat = [[0,0],[0,1]]
# 输出: 1
# 
# 
# 示例 3:
# 
# 
# 
# 
# 输入: mat = [[0,0],[0,0]]
# 输出: -1
# 
# 示例 4:
# 
# 
# 
# 
# 输入: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# 输出: 1
# 
# 
# 
# 
# 提示:
# 
# 
# rows == mat.length
# cols == mat[i].length
# 1 <= rows, cols <= 100
# mat[i][j] 只会是 0 或 1。
# mat[i] 已按非递减顺序排序。
# 
# 
#

# @lc code=start
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        res = 0x7fffffff
        m, n = binaryMatrix.dimensions()
        for i in range(m):
            l, r = 0, n - 1
            p = -1
            while l <= r:
                m = l + (r - l) // 2
                v = binaryMatrix.get(i, m)

                if v == 1:
                    p, r = m, m - 1
                else:
                    l = m + 1

            if p != -1:
                res = min(res, p)

        return -1 if res == 0x7fffffff else res

# @lc code=end
