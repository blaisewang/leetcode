#
# @lc app=leetcode.cn id=548 lang=python3
#
# [548] 将数组分割成和相等的子数组
#
# https://leetcode-cn.com/problems/split-array-with-equal-sum/description/
#
# algorithms
# Medium (33.92%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 3.3K
# Testcase Example:  '[1,2,1,2,1,2,1]'
#
# 给定一个有 n 个整数的数组，你需要找到满足以下条件的三元组 (i, j, k) ：
# 
# 
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# 子数组 (0, i - 1)，(i + 1, j - 1)，(j + 1, k - 1)，(k + 1, n - 1) 的和应该相等。
# 
# 
# 这里我们定义子数组 (L, R) 表示原数组从索引为L的元素开始至索引为R的元素。
# 
# 
# 
# 示例:
# 
# 输入: [1,2,1,2,1,2,1]
# 输出: True
# 解释:
# i = 1, j = 3, k = 5. 
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# 
# 
# 
# 
# 注意:
# 
# 
# 1 <= n <= 2000。
# 给定数组中的元素会在 [-1,000,000, 1,000,000] 范围内。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 7:
            return False

        s = [nums[0]]
        for i in range(1, n):
            s.append(s[i - 1] + nums[i])

        for j in range(3, n - 3):
            ss = set()
            for i in range(1, j - 1):
                if s[i - 1] == s[j - 1] - s[i]:
                    ss.add(s[i - 1])
            for k in range(j + 2, n - 1):
                if s[n - 1] - s[k] == s[k - 1] - s[j] and s[k - 1] - s[j] in ss:
                    return True

        return False

# @lc code=end
