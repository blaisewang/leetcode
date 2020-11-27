#
# @lc app=leetcode.cn id=247 lang=python3
#
# [247] 中心对称数 II
#
# https://leetcode-cn.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (50.31%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    2.5K
# Total Submissions: 5.1K
# Testcase Example:  '2'
#
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。
# 
# 找到所有长度为 n 的中心对称数。
# 
# 示例 :
# 
# 输入:  n = 2
# 输出: ["11","69","88","96"]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        f = {-1: [], 0: [""], 1: ["0", "1", "8"], 2: ["11", "69", "88", "96"]}
        if n == 0 or n == 1 or n == 2:
            return f[n]

        for i in range(3, n + 1):
            f[i - 2].extend([f"0{m}0" for m in f[i - 4]])
            f[i] = [k for m in f[i - 2] for k in [f"1{m}1", f"6{m}9", f"8{m}8", f"9{m}6"]]

        return f[n]

# @lc code=end
