#
# @lc app=leetcode.cn id=681 lang=python3
#
# [681] 最近时刻
#
# https://leetcode-cn.com/problems/next-closest-time/description/
#
# algorithms
# Medium (49.89%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    1.6K
# Total Submissions: 3.2K
# Testcase Example:  '"19:34"'
#
# 给定一个形如 “HH:MM” 表示的时刻，利用当前出现过的数字构造下一个距离当前时间最近的时刻。每个出现数字都可以被无限次使用。
# 
# 你可以认为给定的字符串一定是合法的。例如，“01:34” 和 “12:09” 是合法的，“1:34” 和 “12:9” 是不合法的。
# 
# 
# 
# 样例 1:
# 
# 输入: "19:34"
# 输出: "19:39"
# 解释: 利用数字 1, 9, 3, 4 构造出来的最近时刻是 19:39，是 5 分钟之后。结果不是 19:33 因为这个时刻是 23 小时 59
# 分钟之后。
# 
# 
# 
# 
# 样例 2:
# 
# 输入: "23:59"
# 输出: "22:22"
# 解释: 利用数字 2, 3, 5, 9 构造出来的最近时刻是 22:22。 答案一定是第二天的某一时刻，所以选择可构造的最小时刻。
# 
# 
# 
# 
#

# @lc code=start
from itertools import product


class Solution:
    def nextClosestTime(self, time: str) -> str:
        def td(l: list) -> float:
            h, m = int("".join(l[:2])), int("".join(l[2:]))
            if h > 23 or m > 59:
                return float("inf")
            else:
                d = (h - hour) * 60 + m - minutes
                if d <= 0:
                    d += 24 * 60
                return d

        diff = float("inf")
        hour, minutes = [int(s) for s in time.split(":")]
        digits = set(list("".join(time.split(":"))))
        res = None
        for lst in product(digits, repeat=4):
            t = td(lst)
            if t < diff:
                diff = t
                res = f"{lst[0] + lst[1]}:{lst[2] + lst[3]}"

        return res

# @lc code=end
