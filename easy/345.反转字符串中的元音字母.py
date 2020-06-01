#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (48.25%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 40K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 示例 1:
# 
# 输入: "hello"
# 输出: "holle"
# 
# 
# 示例 2:
# 
# 输入: "leetcode"
# 输出: "leotcede"
# 
# 说明:
# 元音字母不包含字母"y"。
# 
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)
        i, j = 0, len(s) - 1
        v = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        while i < j:

            while s[i] not in v and i < j:
                i += 1
            while s[j] not in v and i < j:
                j -= 1

            if i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1

        return "".join(s)

# @lc code=end
