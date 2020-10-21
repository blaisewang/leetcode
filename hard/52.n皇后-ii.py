#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (79.16%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    34.9K
# Total Submissions: 43.5K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 
# 示例:
# 
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
# 
# 
# 提示：
# 
# 
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或
# N-1 步，可进可退。（引用自 百度百科 - 皇后 ）
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        c = 0
        col = [0] * n
        diag = [0] * (2 * n - 1)
        anti_diag = [0] * (2 * n - 1)

        def get_res(i):
            nonlocal c
            if i == n:
                c += 1
                return
            for j in range(n):
                if col[j] or diag[i - j] or anti_diag[i + j]:
                    continue
                col[j] = diag[i - j] = anti_diag[i + j] = 1
                get_res(i + 1)
                col[j] = diag[i - j] = anti_diag[i + j] = 0

        get_res(0)
        return c

# @lc code=end
