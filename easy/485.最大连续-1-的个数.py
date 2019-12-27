#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#
# https://leetcode-cn.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (54.99%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    24.5K
# Total Submissions: 44.4K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# 给定一个二进制数组， 计算其中最大连续1的个数。
# 
# 示例 1:
# 
# 
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 
# 
# 注意：
# 
# 
# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # return max(map(len, "".join(map(str, nums)).split("0")))

        c = max_c = 0
        for n in nums:
            if n == 1:
                c += 1
            else:
                max_c = max(max_c, c)
                c = 0
        return max(max_c, c)

# @lc code=end
