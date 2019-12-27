#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# https://leetcode-cn.com/problems/keyboard-row/description/
#
# algorithms
# Easy (67.83%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    12.7K
# Total Submissions: 18.7K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
# 
# 
# 
# 
# 
# 
# 
# 示例：
# 
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
# 
# 
# 
# 
# 注意：
# 
# 
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。
# 
#

# @lc code=start
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        second = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
        third = {"z", "x", "c", "v", "b", "n", "m"}

        r = []

        for word in words:
            c_set = set(word.lower())

            if c_set <= first or c_set <= second or c_set <= third:
                r.append(word)

        return r

    # @lc code=end
