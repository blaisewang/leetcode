#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (41.52%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    63.9K
# Total Submissions: 153.7K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans("", "", string.punctuation))
        s = s.replace(" ", "").lower()

        return s[::-1] == s

# @lc code=end
