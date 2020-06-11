#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#
# https://leetcode-cn.com/problems/binary-gap/description/
#
# algorithms
# Easy (59.20%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 15.6K
# Testcase Example:  '22'
#
# 给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。 
# 
# 如果没有两个连续的 1，返回 0 。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：22
# 输出：2
# 解释：
# 22 的二进制是 0b10110 。
# 在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
# 第一对连续的 1 中，两个 1 之间的距离为 2 。
# 第二对连续的 1 中，两个 1 之间的距离为 1 。
# 答案取两个距离之中最大的，也就是 2 。
# 
# 
# 示例 2：
# 
# 输入：5
# 输出：2
# 解释：
# 5 的二进制是 0b101 。
# 
# 
# 示例 3：
# 
# 输入：6
# 输出：1
# 解释：
# 6 的二进制是 0b110 。
# 
# 
# 示例 4：
# 
# 输入：8
# 输出：0
# 解释：
# 8 的二进制是 0b1000 。
# 在 8 的二进制表示中没有连续的 1，所以返回 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def binaryGap(self, N: int) -> int:
        l, r = None, 0
        for i in range(32):
            if (N >> i) & 1:
                if l is not None:
                    r = max(r, i - l)
                l = i
        return r

# @lc code=end
