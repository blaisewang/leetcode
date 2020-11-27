#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#
# https://leetcode-cn.com/problems/image-smoother/description/
#
# algorithms
# Easy (51.43%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 15K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入)
# ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
# 
# 示例 1:
# 
# 
# 输入:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# 输出:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# 解释:
# 对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
# 对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
# 对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
# 
# 
# 注意:
# 
# 
# 给定矩阵中的整数范围为 [0, 255]。
# 矩阵的长和宽的范围均为 [1, 150]。
# 
# 
#

# @lc code=start
from typing import List


class Solution:

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        max_r, max_c = len(M), len(M[0])
        m = [[0] * max_c for _ in range(max_r)]

        for r in range(max_r):
            for c in range(max_c):
                count = 0
                for tr in (r - 1, r, r + 1):
                    for tc in (c - 1, c, c + 1):
                        if 0 <= tr < max_r and 0 <= tc < max_c:
                            m[r][c] += M[tr][tc]
                            count += 1
                m[r][c] = m[r][c] // count

        return m

# @lc code=end
