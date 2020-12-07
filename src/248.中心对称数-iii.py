#
# @lc app=leetcode.cn id=248 lang=python3
#
# [248] 中心对称数 III
#
# https://leetcode-cn.com/problems/strobogrammatic-number-iii/description/
#
# algorithms
# Hard (42.56%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 3.5K
# Testcase Example:  '"50"\n"100"'
#
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
# 
# 写一个函数来计算范围在 [low, high] 之间中心对称数的个数。
# 
# 示例:
# 
# 输入: low = "50", high = "100"
# 输出: 3 
# 解释: 69，88 和 96 是三个在该范围内的中心对称数
# 
# 注意:
# 由于范围可能很大，所以 low 和 high 都用字符串表示。
# 
#

# @lc code=start
from typing import List


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        l, h = int(low), int(high)
        r = set()

        if int(l) < 10:
            for k in [0, 1, 8]:
                if l <= k <= h:
                    r.add(k)

        def helper(n: int) -> List[str]:
            nonlocal r
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]

            res = []
            for i in helper(n - 2):
                for k, v in d.items():
                    t = v + i + k
                    res.append(t)
                    if len(str(int(t))) == n and l <= int(t) <= h:
                        r.add(t)

            return res

        helper(len(high))
        helper(len(high) - 1)

        return len(r)

# @lc code=end
