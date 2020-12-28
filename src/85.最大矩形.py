#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (48.80%)
# Likes:    685
# Dislikes: 0
# Total Accepted:    49.8K
# Total Submissions: 101.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：matrix = [["0","0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 0 
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        ds = [0] * len(matrix[0])
        r = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    ds[j] = 0
                else:
                    ds[j] += 1

            s = list(set(ds))
            for idx1 in range(len(s)):
                ml, cl = 0, 0
                for idx2 in range(len(matrix[0])):
                    if ds[idx2] >= s[idx1]:
                        cl += 1
                    else:
                        r = max(r, cl * s[idx1])
                        cl = 0
                    ml = max(ml, cl)
                r = max(r, ml * s[idx1])

        return r

# @lc code=end
