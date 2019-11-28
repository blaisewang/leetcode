#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.34%)
# Likes:    775
# Dislikes: 0
# Total Accepted:    150.3K
# Total Submissions: 425.2K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""
        min_len = len(min(strs, key=len, default=""))

        for i in range(min_len):
            if all(x[i] == strs[0][i] for x in strs):
                prefix += strs[0][i]
            else:
                return prefix

        return prefix

# @lc code=end
