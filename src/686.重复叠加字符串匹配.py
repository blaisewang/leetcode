#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#
# https://leetcode-cn.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (32.55%)
# Likes:    82
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 29.6K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
# 
# 举个例子，A = "abcd"，B = "cdabcdab"。
# 
# 答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
# 
# 注意:
# 
# A 与 B 字符串的长度在1和10000区间范围内。
# 
#


# @lc code=start
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        x, y = len(A), len(B)
        for i in range(y // x, (y + 2 * x - 2) // x + 1):
            if B in A * i:
                return i

        return -1

# @lc code=end
