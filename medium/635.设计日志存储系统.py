#
# @lc app=leetcode.cn id=635 lang=python3
#
# [635] 设计日志存储系统
#
# https://leetcode-cn.com/problems/design-log-storage-system/description/
#
# algorithms
# Medium (53.39%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 4.3K
# Testcase Example:  '["LogSystem","put","put","put","retrieve","retrieve"]\n[[],[1,"2017:01:01:23:59:59"],[2,"2017:01:01:22:59:59"],[3,"2016:01:01:00:00:00"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Year"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"]]'
#
# 你将获得多条日志，每条日志都有唯一的 id 和 timestamp ，timestamp 是形如
# Year:Month:Day:Hour:Minute:Second 的字符串，2017:01:01:23:59:59 ，所有值域都是零填充的十进制数。
# 
# 实现 LogSystem 类：
# 
# 
# LogSystem() 初始化 LogSystem 对象
# void put(int id, string timestamp) 给定日志的 id 和 timestamp ，将这个日志存入你的存储系统中。
# int[] retrieve(string start, string end, string granularity) 返回在给定时间区间
# [start, end] （包含两端）内的所有日志的 id 。start 、end 和 timestamp 的格式相同，granularity
# 表示考虑的时间粒度（例如，精确到 Day、Minute 等）。例如 start = "2017:01:01:23:59:59"、end =
# "2017:01:02:23:59:59" 且 granularity = "Day" 意味着需要查找从 Jan. 1st 2017 到 Jan. 2nd
# 2017 范围内的日志，可以忽略日志的 Hour、Minute 和 Second 。
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
# [[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3,
# "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00",
# "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
# 输出：
# [null, null, null, null, [3, 2, 1], [2, 1]]
# 
# 解释：
# LogSystem logSystem = new LogSystem();
# logSystem.put(1, "2017:01:01:23:59:59");
# logSystem.put(2, "2017:01:01:22:59:59");
# logSystem.put(3, "2016:01:01:00:00:00");
# 
# // 返回 [3,2,1]，返回从 2016 年到 2017 年所有的日志。
# logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");
# 
# // 返回 [2,1]，返回从 Jan. 1, 2016 01:XX:XX 到 Jan. 1, 2017 23:XX:XX 之间的所有日志
# // 不返回日志 3 因为记录时间 Jan. 1, 2016 00:00:00 超过范围的起始时间
# logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00",
# "Hour");
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 2000 
# 1 
# 1 
# 0 
# 0 
# granularity 是这些值 ["Year", "Month", "Day", "Hour", "Minute", "Second"] 之一
# 最多调用 500 次 put 和 retrieve
# 
# 
#

# @lc code=start
from typing import List


class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        bm = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}
        bn = bm.get(granularity)

        r = []
        for log in self.logs:
            if start[:bn] <= log[1][:bn] <= end[:bn]:
                r.append(log[0])

        return r

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
# @lc code=end
