#
# @lc app=leetcode.cn id=1010 lang=python3
#
# [1010] 总持续时间可被 60 整除的歌曲
#
# https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (42.32%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 28.9K
# Testcase Example:  '[30,20,150,100,40]'
#
# 在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
# 
# 返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望索引的数字 i 和 j 满足  i < j 且有 (time[i] +
# time[j]) % 60 == 0。
# 
# 
# 
# 示例 1：
# 
# 输入：[30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整数：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60
# 
# 
# 示例 2：
# 
# 输入：[60,60,60]
# 输出：3
# 解释：所有三对的总持续时间都是 120，可以被 60 整数。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = 0
        t = [0] * 60
        for i in range(len(time)):
            n += t[(60 - time[i] % 60) % 60]
            t[time[i] % 60] += 1
        return n

# @lc code=end
