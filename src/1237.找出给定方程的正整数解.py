#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#
# https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation/description/
#
# algorithms
# Easy (66.99%)
# Likes:    25
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 8.3K
# Testcase Example:  '1\n5'
#
# 给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。
# 
# 给定函数是严格单调的，也就是说：
# 
# 
# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)
# 
# 
# 函数接口定义如下：
# 
# interface CustomFunction {
# public:
# // Returns positive integer f(x, y) for any given positive integer x and y.
# int f(int x, int y);
# };
# 
# 
# 如果你想自定义测试，你可以输入整数 function_id 和一个目标结果 z 作为输入，其中 function_id
# 表示一个隐藏函数列表中的一个函数编号，题目只会告诉你列表中的 2 个函数。  
# 
# 你可以将满足条件的 结果数对 按任意顺序返回。
# 
# 
# 
# 示例 1：
# 
# 输入：function_id = 1, z = 5
# 输出：[[1,4],[2,3],[3,2],[4,1]]
# 解释：function_id = 1 表示 f(x, y) = x + y
# 
# 示例 2：
# 
# 输入：function_id = 2, z = 5
# 输出：[[1,5],[5,1]]
# 解释：function_id = 2 表示 f(x, y) = x * y
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= function_id <= 9
# 1 <= z <= 100
# 题目保证 f(x, y) == z 的解处于 1 <= x, y <= 1000 的范围内。
# 在 1 <= x, y <= 1000 的前提下，题目保证 f(x, y) 是一个 32 位有符号整数。
# 
# 
#

# @lc code=start
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        r, x, y = [], 1, 1000
        while x <= z and y >= 1:
            rt = customfunction.f(x, y)
            if rt < z:
                x += 1
            elif rt > z:
                y -= 1
            if rt == z:
                r.append([x, y])
                x += 1
                y -= 1
        return r

# @lc code=end
