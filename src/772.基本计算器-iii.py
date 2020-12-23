#
# @lc app=leetcode.cn id=772 lang=python3
#
# [772] 基本计算器 III
#
# https://leetcode-cn.com/problems/basic-calculator-iii/description/
#
# algorithms
# Hard (41.62%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 6.5K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算简单的表达式字符串。
# 
# 表达式字符串只包含非负整数， +, -, *, / 操作符，左括号 ( ，右括号 )和空格 。整数除法需要向下截断。
# 
# 你可以假定给定的字符串总是有效的。所有的中间结果的范围为 [-2147483648, 2147483647]。
# 
# 进阶：你可以在不使用内置库函数的情况下解决此问题吗？
# 
# 
# 
# 示例 1：
# 
# 输入：s = "1 + 1"
# 输出：2
# 
# 
# 示例 2：
# 
# 输入：s = " 6-4 / 2 "
# 输出：4
# 
# 
# 示例 3：
# 
# 输入：s = "2*(5+5*2)/3+(6/2+8)"
# 输出：21
# 
# 
# 示例 4：
# 
# 输入：s = "(2+6* 3+5- (3*14/7+2)*5)+3"
# 输出：-12
# 
# 
# 示例 5：
# 
# 输入：s = "0"
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s <= 10^4
# s 由整数、'+'、'-'、'*'、'/'、'('、')' 和 ' ' 组成
# s 是一个 有效的 表达式
# 
# 
#

# @lc code=start
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def recur(sl):
            stack = []
            sign = "+"
            num = 0

            while len(sl) > 0:
                c = sl.popleft()
                if c.isdigit():
                    num = 10 * num + int(c)

                if c == "(":
                    num = recur(sl)

                if c in "+-*/()" or not sl:
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    elif sign == "/":
                        stack.append(int(stack.pop() / num))
                    num = 0
                    sign = c

                if c == ")":
                    break
            return sum(stack)

        return recur(deque(list(s)))

# @lc code=end
