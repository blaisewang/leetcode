#
# @lc app=leetcode.cn id=1198 lang=python3
#
# [1198] 找出所有行中最小公共元素
#
# https://leetcode-cn.com/problems/find-smallest-common-element-in-all-rows/description/
#
# algorithms
# Medium (74.41%)
# Likes:    12
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 3.9K
# Testcase Example:  '[[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]'
#
# 给你一个矩阵 mat，其中每一行的元素都已经按 递增 顺序排好了。请你帮忙找出在所有这些行中 最小的公共元素。
# 
# 如果矩阵中没有这样的公共元素，就请返回 -1。
# 
# 
# 
# 示例：
# 
# 输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= mat.length, mat[i].length <= 500
# 1 <= mat[i][j] <= 10^4
# mat[i] 已按递增顺序排列。
# 
# 
#

# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        res = reduce(lambda i, j: i & j, [set(v) for v in mat])
        return min(res) if res else -1

# @lc code=end
