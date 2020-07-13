#
# @lc app=leetcode.cn id=254 lang=python3
#
# [254] 因子的组合
#
# https://leetcode-cn.com/problems/factor-combinations/description/
#
# algorithms
# Medium (56.46%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 3.4K
# Testcase Example:  '1'
#
# 整数可以被看作是其因子的乘积。
# 
# 例如：
# 
# 8 = 2 x 2 x 2;
# ⁠ = 2 x 4.
# 
# 请实现一个函数，该函数接收一个整数 n 并返回该整数所有的因子组合。
# 
# 注意：
# 
# 
# 你可以假定 n 为永远为正数。
# 因子必须大于 1 并且小于 n。
# 
# 
# 示例 1：
# 
# 输入: 1
# 输出: []
# 
# 
# 示例 2：
# 
# 输入: 37
# 输出: []
# 
# 示例 3：
# 
# 输入: 12
# 输出:
# [
# ⁠ [2, 6],
# ⁠ [2, 2, 3],
# ⁠ [3, 4]
# ]
# 
# 示例 4: 
# 
# 输入: 32
# 输出:
# [
# ⁠ [2, 16],
# ⁠ [2, 2, 8],
# ⁠ [2, 2, 2, 4],
# ⁠ [2, 2, 2, 2, 2],
# ⁠ [2, 4, 4],
# ⁠ [4, 8]
# ]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []

        def backtrack(r, i, c):
            for j in range(i, int(r ** 0.5) + 1):
                if r % j == 0:
                    res.append(sorted(c + [r // j, j]))
                    backtrack(r // j, j, [j] + c)

        backtrack(n, 2, [])
        return res

# @lc code=end
