#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (43.81%)
# Likes:    760
# Dislikes: 0
# Total Accepted:    134.9K
# Total Submissions: 306.3K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
# 
# 
# 
# 提示：
# 
# 
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def helper(ci: int, cj: int, k: int, visited: Set[tuple]) -> bool:
            if k == len(word):
                return True

            for x, y in {(-1, 0), (1, 0), (0, 1), (0, -1)}:
                ti = x + ci
                tj = y + cj
                if 0 <= ti < row and 0 <= tj < col and (ti, tj) not in visited and board[ti][tj] == word[k]:
                    visited.add((ti, tj))
                    if helper(ti, tj, k + 1, visited):
                        return True
                    visited.remove((ti, tj))

            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):
                    return True

        return False

# @lc code=end
