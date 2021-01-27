#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (78.43%)
# Likes:    293
# Dislikes: 0
# Total Accepted:    58.5K
# Total Submissions: 74.5K
# Testcase Example:  '3'
#
# 给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 
# 示例:
# 
# 输入: 3
# 输出:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
#

# @lc code=start
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r, n = [[n ** 2]], n ** 2
        while n > 1:
            n, r = n - len(r), [[*range(n - len(r), n)]] + [*zip(*r[::-1])]
        return r

# @lc code=end
