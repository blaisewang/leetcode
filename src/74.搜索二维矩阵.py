#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# https://leetcode-cn.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (39.31%)
# Likes:    303
# Dislikes: 0
# Total Accepted:    79.3K
# Total Submissions: 198.5K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 
# 
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -10^4 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        l, r = 0, len(matrix) * len(matrix[0]) - 1
        a = [column for row in matrix for column in row]
        while l <= r:
            m = ((r - l) >> 1) + l
            if a[m] == target:
                return True
            elif a[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

# @lc code=end
