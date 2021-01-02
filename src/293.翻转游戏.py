#
# @lc app=leetcode.cn id=293 lang=python3
#
# [293] 翻转游戏
#
# https://leetcode-cn.com/problems/flip-game/description/
#
# algorithms
# Easy (70.66%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 5K
# Testcase Example:  '"++++"'
#
# 你和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。
# 当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。
# 
# 请你写出一个函数，来计算出第一次翻转后，字符串所有的可能状态。
# 
# 
# 
# 示例：
# 
# 输入: s = "++++"
# 输出: 
# [
# ⁠ "--++",
# ⁠ "+--+",
# ⁠ "++--"
# ]
# 
# 
# 注意：如果不存在可能的有效操作，请返回一个空列表 []。
# 
#

# @lc code=start
from typing import List


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        return [s[:i] + "--" + s[i + 2:] for i in range(len(s) - 1) if s[i] == s[i + 1] == "+"]

# @lc code=end
