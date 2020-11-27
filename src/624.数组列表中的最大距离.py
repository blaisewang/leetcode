#
# @lc app=leetcode.cn id=624 lang=python3
#
# [624] 数组列表中的最大距离
#
# https://leetcode-cn.com/problems/maximum-distance-in-arrays/description/
#
# algorithms
# Medium (40.63%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 4.1K
# Testcase Example:  '[[1,2,3],[4,5],[1,2,3]]'
#
# 给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b
# 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离
# 
# 示例 1：
# 
# 输入： 
# [[1,2,3],
# ⁠[4,5],
# ⁠[1,2,3]]
# 输出： 4
# 解释：
# 一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
# 
# 
# 
# 
# 注意：
# 
# 
# 每个给定数组至少会有 1 个数字。列表中至少有两个非空数组。
# 所有 m 个数组中的数字总数目在范围 [2, 10000] 内。
# m 个数组中所有整数的范围在 [-10000, 10000] 内。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        r = 0
        min_val = arrays[0][0]
        max_val = arrays[0][len(arrays[0]) - 1]

        for i in range(1, len(arrays)):
            r = max(r, max(abs(arrays[i][len(arrays[i]) - 1] - min_val), abs(arrays[i][0] - max_val)))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][len(arrays[i]) - 1])

        return r

# @lc code=end

