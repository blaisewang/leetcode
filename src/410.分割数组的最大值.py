#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
# https://leetcode-cn.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (43.77%)
# Likes:    186
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 18.5K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
# 
# 注意:
# 数组长度 n 满足以下条件:
# 
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 示例: 
# 
# 
# 输入:
# nums = [7,2,5,10,8]
# m = 2
# 
# 输出:
# 18
# 
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x: int) -> bool:
            t, c = 0, 1
            for n in nums:
                if t + n > x:
                    c += 1
                    t = n
                else:
                    t += n
            return c <= m

        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
        
# @lc code=end

