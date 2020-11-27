#
# @lc app=leetcode.cn id=320 lang=python3
#
# [320] 列举单词的全部缩写
#
# https://leetcode-cn.com/problems/generalized-abbreviation/description/
#
# algorithms
# Medium (65.49%)
# Likes:    19
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 2.2K
# Testcase Example:  '"word"'
#
# 请你写出一个能够举单词全部缩写的函数。
# 
# 注意：输出的顺序并不重要。
# 
# 示例：
# 
# 输入: "word"
# 输出:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        r = []

        def backtrace(c: str, i: int):
            if i == len(word):
                r.append(c)
                return

            backtrace(c + word[i], i + 1)
            if not (c and c[-1].isdigit()):
                for j in range(i, len(word)):
                    backtrace(c + str(j - i + 1), j + 1)

        backtrace("", 0)
        return r

# @lc code=end
