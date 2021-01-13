#
# @lc app=leetcode.cn id=1180 lang=python3
#
# [1180] 统计只含单一字母的子串
#
# https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter/description/
#
# algorithms
# Easy (75.98%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 3.2K
# Testcase Example:  '"aaaba"'
#
# 给你一个字符串 S，返回只含 单一字母 的子串个数。
# 
# 示例 1：
# 
# 输入： "aaaba"
# 输出： 8
# 解释： 
# 只含单一字母的子串分别是 "aaa"， "aa"， "a"， "b"。
# "aaa" 出现 1 次。
# "aa" 出现 2 次。
# "a" 出现 4 次。
# "b" 出现 1 次。
# 所以答案是 1 + 2 + 4 + 1 = 8。
# 
# 
# 示例 2:
# 
# 输入： "aaaaaaaaaa"
# 输出： 55
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= S.length <= 1000
# S[i] 仅由小写英文字母组成。
# 
# 
#

# @lc code=start
class Solution:
    def countLetters(self, S: str) -> int:
        s = S + "!"
        c, t = 1, 0
        for i in range(len(s) - 1):
            if s[i + 1] != s[i]:
                t += (c + 1) * c // 2
                c = 1
            else:
                c += 1

        return t

# @lc code=end
