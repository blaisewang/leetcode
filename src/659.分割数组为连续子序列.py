#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#
# https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (42.83%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 12.4K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。
# 
# 如果可以完成上述分割，则返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入: [1,2,3,3,4,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3
# 3, 4, 5
# 
# 
# 
# 
# 示例 2：
# 
# 输入: [1,2,3,3,4,4,5,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
# 
# 
# 
# 示例 3：
# 
# 输入: [1,2,3,4,4,5]
# 输出: False
# 
# 
# 
# 
# 提示：
# 
# 
# 输入的数组长度范围为 [1, 10000]
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cm = Counter(nums)
        em = Counter()

        for n in nums:
            if cm[n] > 0:
                if (prevEndCount := em.get(n - 1, 0)) > 0:
                    cm[n] -= 1
                    em[n - 1] = prevEndCount - 1
                    em[n] += 1
                else:
                    if cm.get(n + 1, 0) > 0 and cm.get(n + 2, 0) > 0:
                        cm[n] -= 1
                        cm[n + 1] -= 1
                        cm[n + 2] -= 1
                        em[n + 2] += 1
                    else:
                        return False

        return True

# @lc code=end
