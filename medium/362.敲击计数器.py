#
# @lc app=leetcode.cn id=362 lang=python3
#
# [362] 敲击计数器
#
# https://leetcode-cn.com/problems/design-hit-counter/description/
#
# algorithms
# Medium (67.38%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 1.9K
# Testcase Example:  '["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]\n' + '[[],[1],[2],[3],[4],[300],[300],[301]]'
#
# 设计一个敲击计数器，使它可以统计在过去5分钟内被敲击次数。
# 
# 每个函数会接收一个时间戳参数（以秒为单位），你可以假设最早的时间戳从1开始，且都是按照时间顺序对系统进行调用（即时间戳是单调递增）。
# 
# 在同一时刻有可能会有多次敲击。
# 
# 示例:
# 
# HitCounter counter = new HitCounter();
# 
# // 在时刻 1 敲击一次。
# counter.hit(1);
# 
# // 在时刻 2 敲击一次。
# counter.hit(2);
# 
# // 在时刻 3 敲击一次。
# counter.hit(3);
# 
# // 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
# counter.getHits(4);
# 
# // 在时刻 300 敲击一次。
# counter.hit(300);
# 
# // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
# counter.getHits(300);
# 
# // 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
# counter.getHits(301); 
# 
# 
# 进阶:
# 
# 如果每秒的敲击次数是一个很大的数字，你的计数器可以应对吗？
# 
#

# @lc code=start
import bisect
from collections import deque


class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = deque(maxlen=301)
        self.tsa = deque(maxlen=301)
        self.ts.append(0)
        self.tsa.append(0)

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp == self.ts[-1]:
            self.tsa[-1] += 1
        else:
            self.ts.append(timestamp)
            self.tsa.append(self.tsa[-1] + 1)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        return self.tsa[max(bisect.bisect_right(self.ts, timestamp) - 1, 0)] - self.tsa[max(bisect.bisect_left(self.ts, timestamp - 299) - 1, 0)]

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
# @lc code=end
