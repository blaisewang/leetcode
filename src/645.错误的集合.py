#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
# https://leetcode-cn.com/problems/set-mismatch/description/
#
# algorithms
# Easy (39.29%)
# Likes:    93
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 34.9K
# Testcase Example:  '[1,2,2,4]'
#
# 集合 S 包含从1到 n
# 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
# 
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
# 
# 
# 注意:
# 
# 
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = 0
        res = list(set(nums) ^ set((range(1, len(nums) + 1))))
        for n in nums:
            c ^= n
        for i in range(1, len(nums) + 1):
            c ^= i
        a = res[0] ^ c
        return [a, res[0]]

# @lc code=end
