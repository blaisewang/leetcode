#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (43.70%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 64.6K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "bcabc"
# 输出："abc"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = ["0"]
        for i, c in enumerate(s):
            if c not in stk:
                while c < stk[-1] and stk[-1] in s[i + 1:]:
                    stk.pop()
                stk.append(c)

        return "".join(stk[1:])

# @lc code=end
