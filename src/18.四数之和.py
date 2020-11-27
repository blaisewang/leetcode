#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (36.25%)
# Likes:    509
# Dislikes: 0
# Total Accepted:    88.8K
# Total Submissions: 234.4K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        d, r = dict(), set()

        for i in range(n - 1):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                if target - s in d:
                    for t in d[target - s]:
                        if t[1] < i:
                            r.add((nums[t[0]], nums[t[1]], nums[i], nums[j]))
                if s not in d:
                    d[s] = []
                d[s].append((i, j))

        return [list(rt) for rt in r]

# @lc code=end
