#
# @lc app=leetcode.cn id=1085 lang=python3
#
# [1085] 最小元素各数位之和
#
# https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number/description/
#
# algorithms
# Easy (76.48%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 3.7K
# Testcase Example:  '[34,23,1,24,75,33,54,8]'
#
# 给你一个正整数的数组 A。
# 
# 然后计算 S，使其等于数组 A 当中最小的那个元素各个数位上数字之和。
# 
# 最后，假如 S 所得计算结果是 奇数 的请你返回 0，否则请返回 1。
# 
# 
# 
# 示例 1:
# 
# 输入：[34,23,1,24,75,33,54,8]
# 输出：0
# 解释：
# 最小元素为 1，该元素各个数位上的数字之和 S = 1，是奇数所以答案为 0。
# 
# 
# 示例 2：
# 
# 输入：[99,77,33,66,55]
# 输出：1
# 解释：
# 最小元素为 33，该元素各个数位上的数字之和 S = 3 + 3 = 6，是偶数所以答案为 1。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return 1 - sum(int(i) for i in str(min(A))) % 2

# @lc code=end
