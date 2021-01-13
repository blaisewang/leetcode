#
# @lc app=leetcode.cn id=1213 lang=python3
#
# [1213] 三个有序数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-three-sorted-arrays/description/
#
# algorithms
# Easy (76.27%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 5.9K
# Testcase Example:  '[1,2,3,4,5]\n[1,2,5,7,9]\n[1,3,4,5,8]'
#
# 给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。
# 
# 返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。
# 
# 
# 
# 示例：
# 
# 输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# 输出: [1,5]
# 解释: 只有 1 和 5 同时在这三个数组中出现.
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))

# @lc code=end
