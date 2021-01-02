#
# @lc app=leetcode.cn id=339 lang=python3
#
# [339] 嵌套列表权重和
#
# https://leetcode-cn.com/problems/nested-list-weight-sum/description/
#
# algorithms
# Easy (79.66%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    2.7K
# Total Submissions: 3.4K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给定一个嵌套的整数列表，请返回该列表按深度加权后所有整数的总和。
# 
# 每个元素要么是整数，要么是列表。同时，列表中元素同样也可以是整数或者是另一个列表。
# 
# 示例 1:
# 
# 输入: [[1,1],2,[1,1]]
# 输出: 10 
# 解释: 因为列表中有四个深度为 2 的 1 ，和一个深度为 1 的 2。
# 
# 示例 2:
# 
# 输入: [1,[4,[6]]]
# 输出: 27 
# 解释: 一个深度为 1 的 1，一个深度为 2 的 4，一个深度为 3 的 6。所以，1 + 4*2 + 6*3 = 27。
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from typing import List


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(lst: List[NestedInteger], depth: int) -> int:
            r = 0
            for e in lst:
                if e.getList():
                    r += dfs(e.getList(), depth + 1)
                elif e.getInteger():
                    r += e.getInteger() * depth

            return r

        return dfs(nestedList, 1)

# @lc code=end
