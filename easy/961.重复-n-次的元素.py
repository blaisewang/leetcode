#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#
# https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/description/
#
# algorithms
# Easy (65.90%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    22.8K
# Total Submissions: 34.3K
# Testcase Example:  '[1,2,3,3]'
#
# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
# 
# 返回重复了 N 次的那个元素。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,3]
# 输出：3
# 
# 
# 示例 2：
# 
# 输入：[2,1,2,5,3,2]
# 输出：2
# 
# 
# 示例 3：
# 
# 输入：[5,1,5,2,5,3,5,4]
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 4 <= A.length <= 10000
# 0 <= A[i] < 10000
# A.length 为偶数
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = Counter(A)
        for k in count:
            if count[k] > 1:
                return k

# @lc code=end

