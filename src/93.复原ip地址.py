#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (49.04%)
# Likes:    385
# Dislikes: 0
# Total Accepted:    72.9K
# Total Submissions: 148.6K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 
# 有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
# 
# 
# 
# 示例:
# 
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# 
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        r = []

        def backtrack(t, b):
            if len(t) == 4 and b == len(s):
                r.append('.'.join(t))
            if len(t) == 4 and b < len(s):
                return

            for l in range(1, 4):
                if b + l - 1 >= len(s):
                    return
                if l >= 2 and s[b] == "0":
                    return
                tmp = s[b:b + l]
                if l == 3 and int(tmp) > 255:
                    return
                backtrack(t + [tmp], b + l)

        backtrack([], 0)
        return r

# @lc code=end
