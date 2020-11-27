#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#
# https://leetcode-cn.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (43.80%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 24.6K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
# 
# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
# 
# 示例 1:
# 
# 
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
# 
# 
# 说明: 输入的数组长度最大不超过20,000.
# 
#

# @lc code=start
from collections import Counter

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counter = Counter(nums)
        sorted_keys = list(sorted(counter.keys()))

        candidates = []
        last = sorted_keys[0]
        for i in range(1, len(sorted_keys)):
            if sorted_keys[i] - last == 1:
                candidates.append((last, sorted_keys[i]))
            last = sorted_keys[i]

        return max([counter[x] + counter[y] for x, y in candidates]) if candidates else 0

# @lc code=end
