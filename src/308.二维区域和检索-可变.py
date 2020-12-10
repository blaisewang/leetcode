#
# @lc app=leetcode.cn id=308 lang=python3
#
# [308] 二维区域和检索 - 可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-mutable/description/
#
# algorithms
# Hard (58.73%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 2.4K
# Testcase Example:  '["NumMatrix","sumRegion","update","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[3,2,2],[2,1,4,3]]'
#
# 给你一个 2D 矩阵 matrix，请计算出从左上角 (row1, col1) 到右下角 (row2, col2) 组成的矩形中所有元素的和。
# 
# 
# 上述粉色矩形框内的，该矩形由左上角 (row1, col1) = (2, 1) 和右下角 (row2, col2) = (4, 3)
# 确定。其中，所包括的元素总和 sum = 8。
# 
# 示例：
# 
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# 
# 
# 
# 
# 注意:
# 
# 
# 矩阵 matrix 的值只能通过 update 函数来进行修改
# 你可以默认 update 函数和 sumRegion 函数的调用次数是均匀分布的
# 你可以默认 row1 ≤ row2，col1 ≤ col2
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if matrix == [] or matrix == [[]]:
            return

        row, col = len(matrix), len(matrix[0])

        self.matrix = matrix
        self.ud = defaultdict(int)
        self.sa = [[0] * (col + 1) for _ in range(row + 1)]

        for r in range(row):
            l = 0
            for c in range(col):
                self.sa[r + 1][c + 1] = self.sa[r][c + 1] + l + matrix[r][c]
                l += matrix[r][c]

    def update(self, row: int, col: int, val: int) -> None:
        self.ud[(row, col)] = val - self.matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p1 = self.sa[row2 + 1][col2 + 1]
        p2 = self.sa[row2 + 1][col1]
        p3 = self.sa[row1][col2 + 1]
        p4 = self.sa[row1][col1]

        s = p1 - p2 - p3 + p4
        for (row, col), val in self.ud.items():
            if row1 <= row <= row2 and col1 <= col <= col2:
                s += val

        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
