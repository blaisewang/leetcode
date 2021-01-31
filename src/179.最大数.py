#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (37.51%)
# Likes:    455
# Dislikes: 0
# Total Accepted:    51.1K
# Total Submissions: 135.3K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。
# 
# 注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,2]
# 输出："210"
# 
# 示例 2：
# 
# 
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [1]
# 输出："1"
# 
# 
# 示例 4：
# 
# 
# 输入：nums = [10]
# 输出："10"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = "".join(sorted(map(str, nums), key=LargerNumKey))
        return "0" if largest[0] == "0" else largest

# @lc code=end
