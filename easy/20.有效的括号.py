#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.07%)
# Likes:    1198
# Dislikes: 0
# Total Accepted:    157.1K
# Total Submissions: 392K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        r_l_dict = {")": "(",
                    "}": "{",
                    "]": "["}

        for p in s:
            if p not in r_l_dict:
                stack.append(p)
            else:
                if stack and r_l_dict[p] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True

        return False

# @lc code=end
