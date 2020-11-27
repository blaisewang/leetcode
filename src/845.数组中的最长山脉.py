#
# @lc app=leetcode.cn id=845 lang=python3
#
# [845] 数组中的最长山脉
#
# https://leetcode-cn.com/problems/longest-mountain-in-array/description/
#
# algorithms
# Medium (36.51%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 21.3K
# Testcase Example:  '[2,1,4,7,3,2,5]'
#
# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
# 
# 
# B.length >= 3
# 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... >
# B[B.length - 1]
# 
# 
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
# 
# 给出一个整数数组 A，返回最长 “山脉” 的长度。
# 
# 如果不含有 “山脉” 则返回 0。
# 
# 
# 
# 示例 1：
# 
# 输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
# 
# 
# 示例 2：
# 
# 输入：[2,2,2]
# 输出：0
# 解释：不含 “山脉”。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        res, l = 0, 0
        while l + 2 < n:
            r = l + 1
            if A[l] < A[l + 1]:
                while r + 1 < n and A[r] < A[r + 1]:
                    r += 1
                if r < n - 1 and A[r] > A[r + 1]:
                    while r + 1 < n and A[r] > A[r + 1]:
                        r += 1
                    res = max(res, r - l + 1)
                else:
                    r += 1
            l = r
        return res

# @lc code=end
