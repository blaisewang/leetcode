#
# @lc app=leetcode.cn id=1183 lang=python3
#
# [1183] 矩阵中 1 的最大数量
#
# https://leetcode-cn.com/problems/maximum-number-of-ones/description/
#
# algorithms
# Hard (56.34%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    489
# Total Submissions: 868
# Testcase Example:  '3\n3\n2\n1'
#
# 现在有一个尺寸为 width * height 的矩阵 M，矩阵中的每个单元格的值不是 0 就是 1。
# 
# 而且矩阵 M 中每个大小为 sideLength * sideLength 的 正方形 子阵中，1 的数量不得超过 maxOnes。
# 
# 请你设计一个算法，计算矩阵中最多可以有多少个 1。
# 
# 
# 
# 示例 1：
# 
# 输入：width = 3, height = 3, sideLength = 2, maxOnes = 1
# 输出：4
# 解释：
# 题目要求：在一个 3*3 的矩阵中，每一个 2*2 的子阵中的 1 的数目不超过 1 个。
# 最好的解决方案中，矩阵 M 里最多可以有 4 个 1，如下所示：
# [1,0,1]
# [0,0,0]
# [1,0,1]
# 
# 
# 示例 2：
# 
# 输入：width = 3, height = 3, sideLength = 2, maxOnes = 2
# 输出：6
# 解释：
# [1,0,1]
# [1,0,1]
# [1,0,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= width, height <= 100
# 1 <= sideLength <= width, height
# 0 <= maxOnes <= sideLength * sideLength
# 
# 
#

# @lc code=start
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        a, b = divmod(width, sideLength)
        c, d = divmod(height, sideLength)
        area = b * d
        ac = a * c
        if maxOnes <= area:
            return (ac + a + c + 1) * maxOnes

        res = (ac + a + c + 1) * area
        maxOnes -= area
        if a < c:
            a, b, c, d, width, height = c, d, a, b, height, width

        area = d * (sideLength - b)
        if maxOnes <= area:
            return res + (ac + a) * maxOnes

        res += (ac + a) * area
        maxOnes -= area
        area = b * (sideLength - d)
        if maxOnes <= area:
            return res + (ac + c) * maxOnes

        return res + (ac + c) * area + ac * (maxOnes - area)

# @lc code=end
