#
# @lc app=leetcode.cn id=1087 lang=python3
#
# [1087] 花括号展开
#
# https://leetcode-cn.com/problems/brace-expansion/description/
#
# algorithms
# Medium (50.69%)
# Likes:    28
# Dislikes: 0
# Total Accepted:    1.2K
# Total Submissions: 2.5K
# Testcase Example:  '"{a,b}c{d,e}f"'
#
# 我们用一个特殊的字符串 S 来表示一份单词列表，之所以能展开成为一个列表，是因为这个字符串 S 中存在一个叫做「选项」的概念：
# 
# 单词中的每个字母可能只有一个选项或存在多个备选项。如果只有一个选项，那么该字母按原样表示。
# 
# 如果存在多个选项，就会以花括号包裹来表示这些选项（使它们与其他字母分隔开），例如 "{a,b,c}" 表示 ["a", "b", "c"]。
# 
# 例子："{a,b,c}d{e,f}" 可以表示单词列表 ["ade", "adf", "bde", "bdf", "cde", "cdf"]。
# 
# 请你按字典顺序，返回所有以这种方式形成的单词。
# 
# 
# 
# 示例 1：
# 
# 输入："{a,b}c{d,e}f"
# 输出：["acdf","acef","bcdf","bcef"]
# 
# 
# 示例 2：
# 
# 输入："abcd"
# 输出：["abcd"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= S.length <= 50
# 你可以假设题目中不存在嵌套的花括号
# 在一对连续的花括号（开花括号与闭花括号）之间的所有字母都不会相同
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def expand(self, S: str) -> List[str]:
        i = 0
        r = [""]
        while i < len(S):
            if S[i] == "{":
                j = i
                while S[j] != "}":
                    j += 1
                c = S[i + 1:j].split(",")
                i = j + 1
            else:
                j = i
                while j < len(S) and S[j] != "{":
                    j += 1
                c = [S[i:j]]
                i = j

            r = [i + j for i in r for j in c]

        return sorted(r)

# @lc code=end
