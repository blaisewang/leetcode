#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (72.54%)
# Likes:    1143
# Dislikes: 0
# Total Accepted:    145K
# Total Submissions: 191.5K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:

    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        return [f"({l}){r}" for c in range(n) for l in self.generateParenthesis(c) for r in self.generateParenthesis(n - 1 - c)]

# @lc code=end
