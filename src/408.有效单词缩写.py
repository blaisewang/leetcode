#
# @lc app=leetcode.cn id=408 lang=python3
#
# [408] 有效单词缩写
#
# https://leetcode-cn.com/problems/valid-word-abbreviation/description/
#
# algorithms
# Easy (30.75%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 7.8K
# Testcase Example:  '"internationalization"\n"i12iz4n"'
#
# 给一个 非空 字符串 s 和一个单词缩写 abbr ，判断这个缩写是否可以是给定单词的缩写。
# 
# 字符串 "word" 的所有有效缩写为：
# 
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 注意单词 "word" 的所有有效缩写仅包含以上这些。任何其他的字符串都不是 "word" 的有效缩写。
# 
# 注意:
# 假设字符串 s 仅包含小写字母且 abbr 只包含小写字母和数字。
# 
# 示例 1:
# 
# 给定 s = "internationalization", abbr = "i12iz4n":
# 
# 函数返回 true.
# 
# 
# 
# 
# 示例 2:
# 
# 给定 s = "apple", abbr = "a2e":
# 
# 函数返回 false.
# 
# 
# 
# 
#


# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p, r = 0, 0
        for a in abbr:
            if a.isdigit():
                if r == 0 and a == "0":
                    return False
                r = r * 10 + int(a)
            else:
                p += r
                if p >= len(word) or word[p] != a:
                    return False
                r = 0
                p += 1

        return p + r == len(word)

# @lc code=end
