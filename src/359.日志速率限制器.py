#
# @lc app=leetcode.cn id=359 lang=python3
#
# [359] 日志速率限制器
#
# https://leetcode-cn.com/problems/logger-rate-limiter/description/
#
# algorithms
# Easy (71.00%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 4.5K
# Testcase Example:  '["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]\n[[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]'
#
# 请你设计一个日志系统，可以流式接收日志以及它的时间戳。
# 
# 该日志会被打印出来，需要满足一个条件：当且仅当日志内容 在过去的 10 秒钟内没有被打印过。
# 
# 给你一条日志的内容和它的时间戳（粒度为秒级），如果这条日志在给定的时间戳应该被打印出来，则返回 true，否则请返回 false。
# 
# 要注意的是，可能会有多条日志在同一时间被系统接收。
# 
# 示例：
# 
# Logger logger = new Logger();
# 
# // 日志内容 "foo" 在时刻 1 到达系统
# logger.shouldPrintMessage(1, "foo"); returns true; 
# 
# // 日志内容 "bar" 在时刻 2 到达系统
# logger.shouldPrintMessage(2,"bar"); returns true;
# 
# // 日志内容 "foo" 在时刻 3 到达系统
# logger.shouldPrintMessage(3,"foo"); returns false;
# 
# // 日志内容 "bar" 在时刻 8 到达系统
# logger.shouldPrintMessage(8,"bar"); returns false;
# 
# // 日志内容 "foo" 在时刻 10 到达系统
# logger.shouldPrintMessage(10,"foo"); returns false;
# 
# // 日志内容 "foo" 在时刻 11 到达系统
# logger.shouldPrintMessage(11,"foo"); returns true;
# 
# 
#

# @lc code=start
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timestamp
            return True
        else:
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
# @lc code=end
