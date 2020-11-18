#
# @lc app=leetcode.cn id=1215 lang=python3
#
# [1215] 步进数
#
# https://leetcode-cn.com/problems/stepping-numbers/description/
#
# algorithms
# Medium (38.42%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 3.6K
# Testcase Example:  '0\n21'
#
# 如果一个整数上的每一位数字与其相邻位上的数字的绝对差都是 1，那么这个数就是一个「步进数」。
# 
# 例如，321 是一个步进数，而 421 不是。
# 
# 给你两个整数，low 和 high，请你找出在 [low, high] 范围内的所有步进数，并返回 排序后 的结果。
# 
# 
# 
# 示例：
# 
# 输入：low = 0, high = 21
# 输出：[0,1,2,3,4,5,6,7,8,9,10,12,21]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= low <= high <= 2 * 10^9
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        r = []
        if low <= 0 <= high:
            r.append(0)

        def back_trace(num: str):
            if int(num) > high:
                return

            if low <= int(num) <= high:
                r.append(int(num))

            digit = int(num[-1])
            for d in [digit - 1, digit + 1]:
                if 0 <= d <= 9:
                    back_trace(num + str(d))

        for i in range(1, 10):
            back_trace(str(i))

        return sorted(r)

# @lc code=end
