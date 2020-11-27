#
# @lc app=leetcode.cn id=1060 lang=python3
#
# [1060] 有序数组中的缺失元素
#
# https://leetcode-cn.com/problems/missing-element-in-sorted-array/description/
#
# algorithms
# Medium (51.17%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 4.9K
# Testcase Example:  '[4,7,9,10]\n1'
#
# 给出一个有序数组 A，数组中的每个数字都是 独一无二的，找出从数组最左边开始的第 K 个缺失数字。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [4,7,9,10], K = 1
# 输出：5
# 解释：
# 第一个缺失数字为 5 。
# 
# 
# 示例 2：
# 
# 输入：A = [4,7,9,10], K = 3
# 输出：8
# 解释： 
# 缺失数字有 [5,6,8,...]，因此第三个缺失数字为 8 。
# 
# 
# 示例 3：
# 
# 输入：A = [1,2,4], K = 3
# 输出：6
# 解释：
# 缺失数字有 [3,5,6,7,...]，因此第三个缺失数字为 6 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 50000
# 1 <= A[i] <= 1e7
# 1 <= K <= 1e8
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        m = lambda idx: nums[idx] - nums[0] - idx
        if k > m(len(nums) - 1):
            return nums[-1] + k - m(len(nums) - 1)

        l, r = 0, len(nums) - 1
        while l != r:
            p = l + (r - l) // 2

            if m(p) < k:
                l = p + 1
            else:
                r = p

        return nums[l - 1] + k - m(l - 1)

# @lc code=end
