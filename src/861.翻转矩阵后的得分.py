#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#
# https://leetcode-cn.com/problems/score-after-flipping-matrix/description/
#
# algorithms
# Medium (74.54%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    22.9K
# Total Submissions: 28.3K
# Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
#
# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
# 
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
# 
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
# 
# 返回尽可能高的分数。
# 
# 
# 
# 
# 
# 
# 示例：
# 
# 输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] 是 0 或 1
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        r = n

        for i in range(1, m):
            r <<= 1
            s = sum([A[j][i] ^ A[j][0] for j in range(n)])
            r += max(s, n - s)

        return r

# @lc code=end
