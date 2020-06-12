#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#
# https://leetcode-cn.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (52.50%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    12.9K
# Total Submissions: 23.4K
# Testcase Example:  '"ab-cd"'
#
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入："ab-cd"
# 输出："dc-ba"
# 
# 
# 示例 2：
# 
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
# 
# 
# 示例 3：
# 
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 提示：
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S 中不包含 \ or "
# 
# 
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        r = []
        j = len(r) - 1
        for x in S:
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                r.append(S[j])
                j -= 1
            else:
                r.append(x)

        return "".join(r)

# @lc code=end
