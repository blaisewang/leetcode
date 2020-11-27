#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
# https://leetcode-cn.com/problems/partition-labels/description/
#
# algorithms
# Medium (71.87%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    23.2K
# Total Submissions: 31.8K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
# 
# 
# 
# 示例 1：
# 
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
# 
# 
# 
# 
# 提示：
# 
# 
# S的长度在[1, 500]之间。
# S只包含小写字母 'a' 到 'z' 。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        r = []
        dc = {}
        c, l = 0, 0
        d = {ch: idx for idx, ch in enumerate(S)}
        for i, ch in enumerate(S):
            dc[ch] = i
            if d[ch] == i:
                c += 1
            if len(dc) == c:
                r.append(i - l + 1)
                l = i + 1
                dc = {}
                c = 0

        return r

# @lc code=end
