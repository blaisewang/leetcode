#
# @lc app=leetcode.cn id=346 lang=python3
#
# [346] 数据流中的移动平均值
#
# https://leetcode-cn.com/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (69.29%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 11.4K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。
# 
# 示例:
# 
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
# 
# 
# 
# 
#

# @lc code=start
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = [0] * self.size
        self.head = 0
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum -= self.queue[tail] - val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val

        return self.window_sum / min(self.size, self.count)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end
