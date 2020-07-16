#
# @lc app=leetcode.cn id=294 lang=python3
#
# [294] 翻转游戏 II
#
# https://leetcode-cn.com/problems/flip-game-ii/description/
#
# algorithms
# Medium (57.24%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 3K
# Testcase Example:  '"++++"'
#
# 你和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。
# 当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。
# 
# 请你写出一个函数来判定起始玩家是否存在必胜的方案。
# 
# 示例：
# 
# 输入: s = "++++"
# 输出: true 
# 解析: 起始玩家可将中间的 "++" 翻转变为 "+--+" 从而得胜。
# 
# 
# 延伸：
# 请推导你算法的时间复杂度。
# 
#

# @lc code=start
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def canWin(self, s: str) -> bool:
        length = len(s)
        for i in range(length - 1):
            if s[i] == "+" and s[i + 1] == "+":
                if not self.canWin(f"{s[:i]}--{s[i + 2:]}"):
                    return True
        return False

# @lc code=end
