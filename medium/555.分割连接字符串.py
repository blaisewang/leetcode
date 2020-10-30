#
# @lc app=leetcode.cn id=555 lang=python3
#
# [555] 分割连接字符串
#
# https://leetcode-cn.com/problems/split-concatenated-strings/description/
#
# algorithms
# Medium (32.87%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    837
# Total Submissions: 2.5K
# Testcase Example:  '["abc","xyz"]'
#
# 
# 给定一个字符串列表，你可以将这些字符串连接成一个循环字符串，对于每个字符串，你可以选择是否翻转它。在所有可能的循环字符串中，你需要分割循环字符串（这将使循环字符串变成一个常规的字符串），然后找到字典序最大的字符串。
# 
# 具体来说，要找到字典序最大的字符串，你需要经历两个阶段：
# 
# 
# 将所有字符串连接成一个循环字符串，你可以选择是否翻转某些字符串，并按照给定的顺序连接它们。
# 在循环字符串的某个位置分割它，这将使循环字符串从分割点变成一个常规的字符串。
# 
# 
# 你的工作是在所有可能的常规字符串中找到字典序最大的一个。
# 
# 示例:
# 
# 输入: "abc", "xyz"
# 输出: "zyxcba"
# 解释: 你可以得到循环字符串 "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-"，
# 其中 '-' 代表循环状态。 
# 答案字符串来自第四个循环字符串， 
# 你可以从中间字符 'a' 分割开然后得到 "zyxcba"。
# 
# 
# 
# 
# 注意:
# 
# 
# 输入字符串只包含小写字母。
# 所有字符串的总长度不会超过 1,000。
# 
# 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [s[::-1] if s[::-1] > s else s for s in strs]
        r = "".join(strs)

        for i, s in enumerate(strs):
            rvs = "".join(strs[i + 1:]) + "".join(strs[: i])
            for j, _ in enumerate(s):
                h = s[j:]
                t = s[:j]
                c = h + rvs + t
                r = max(r, c)
                c = t[::-1] + rvs + h[::-1]
                r = max(r, c)

        return r

# @lc code=end
