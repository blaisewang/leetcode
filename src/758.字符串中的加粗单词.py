#
# @lc app=leetcode.cn id=758 lang=python3
#
# [758] 字符串中的加粗单词
#
# https://leetcode-cn.com/problems/bold-words-in-string/description/
#
# algorithms
# Easy (46.15%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 6.8K
# Testcase Example:  '["ab","bc"]\n"aabcd"'
#
# 给定一个关键词集合 words 和一个字符串 S，将所有 S 中出现的关键词加粗。所有在标签 <b> 和 </b> 中的字母都会加粗。
# 
# 返回的字符串需要使用尽可能少的标签，当然标签应形成有效的组合。
# 
# 例如，给定 words = ["ab", "bc"] 和 S = "aabcd"，需要返回 "a<b>abc</b>d"。注意返回
# "a<b>a<b>b</b>c</b>d" 会使用更多的标签，因此是错误的。
# 
# 
# 
# 注：
# 
# 
# words 长度的范围为 [0, 50]。
# words[i] 长度的范围为 [1, 10]。
# S 长度的范围为 [0, 500]。
# 所有 words[i] 和 S 中的字符都为小写字母。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        b = [0] * (len(S) + 1)

        for w in words:
            s = 0
            while s != -1:
                s = S.find(w, s)
                if s != -1:
                    b[s] += 1
                    b[s + len(w)] -= 1
                    s += 1

        s = 0
        r = ""
        for i, e in enumerate(b):
            if s == 0 and e > 0:
                r += "<b>"
            elif s > 0 and s + e == 0:
                r += "</b>"
            if i < len(S):
                r += S[i]
            s += e

        return r

# @lc code=end
