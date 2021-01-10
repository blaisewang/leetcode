#
# @lc app=leetcode.cn id=1119 lang=python3
#
# [1119] 删去字符串中的元音
#
# https://leetcode-cn.com/problems/remove-vowels-from-a-string/description/
#
# algorithms
# Easy (87.02%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    6.5K
# Total Submissions: 7.5K
# Testcase Example:  '"leetcodeisacommunityforcoders"'
#
# 给你一个字符串 S，请你删去其中的所有元音字母（ 'a'，'e'，'i'，'o'，'u'），并返回这个新字符串。
# 
# 
# 
# 示例 1：
# 
# 输入："leetcodeisacommunityforcoders"
# 输出："ltcdscmmntyfrcdrs"
# 
# 
# 示例 2：
# 
# 输入："aeiou"
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# S 仅由小写英文字母组成。
# 1 <= S.length <= 1000
# 
# 
#

# @lc code=start
import re


class Solution:
    def removeVowels(self, s: str) -> str:
        return re.sub(r"[aeiou]", "", s)

# @lc code=end
