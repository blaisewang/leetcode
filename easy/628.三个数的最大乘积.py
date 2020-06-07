#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (48.01%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    20.3K
# Total Submissions: 40.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 
# 示例 1:
# 
# 
# 输入: [1,2,3]
# 输出: 6
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4]
# 输出: 24
# 
# 
# 注意:
# 
# 
# 给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
# 输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
# 
# 
#

# @lc code=start
from heapq import nlargest, nsmallest
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        l3 = nlargest(3, nums)
        s2 = nsmallest(2, nums)

        return max(s2[0] * s2[1] * l3[0], l3[0] * l3[1] * l3[2])

# @lc code=end
