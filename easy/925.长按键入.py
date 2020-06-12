#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#
# https://leetcode-cn.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (44.53%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 22.3K
# Testcase Example:  '"alex"\n"aaleex"'
#
# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
# 
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
# 
# 
# 
# 示例 1：
# 
# 输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex' 中的 'a' 和 'e' 被长按。
# 
# 
# 示例 2：
# 
# 输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
# 
# 
# 示例 3：
# 
# 输入：name = "leelee", typed = "lleeelee"
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：name = "laiden", typed = "laiden"
# 输出：true
# 解释：长按名字中的字符并不是必要的。
# 
# 
# 
# 
# 提示：
# 
# 
# name.length <= 1000
# typed.length <= 1000
# name 和 typed 的字符都是小写字母。
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from itertools import groupby


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        g1, g2 = [[(i, len(list(j))) for i, j in groupby(t)] for t in (name, typed)]
        return len(g1) == len(g2) and all(i[0] == j[0] and i[1] <= j[1] for i, j in zip(g1, g2))

# @lc code=end
