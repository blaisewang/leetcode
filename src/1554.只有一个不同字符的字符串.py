#
# @lc app=leetcode.cn id=1554 lang=python3
#
# [1554] 只有一个不同字符的字符串
#
# https://leetcode-cn.com/problems/strings-differ-by-one-character/description/
#
# algorithms
# Medium (73.83%)
# Likes:    4
# Dislikes: 0
# Total Accepted:    191
# Total Submissions: 258
# Testcase Example:  '["abcd","acbd", "aacd"]'
#
# 给定一个字符串列表 dict ，其中所有字符串的长度都相同。
# 
# 当存在两个字符串在相同索引处只有一个字符不同时，返回 True ，否则返回 False 。
# 
# 进阶：你可以以 O(n*m) 的复杂度解决问题吗？其中 n 是列表 dict 的长度，m 是字符串的长度。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：dict = ["abcd","acbd", "aacd"]
# 输出：true
# 解释：字符串 "abcd" 和 "aacd" 只在索引 1 处有一个不同的字符。
# 
# 
# 示例 2：
# 
# 
# 输入：dict = ["ab","cd","yz"]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：dict = ["abcd","cccc","abyd","abab"]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# dict 中的字符数小于或等于 10^5 。
# dict[i].length == dict[j].length
# dict[i] 是互不相同的。
# dict[i] 只包含小写英文字母。
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        d = Counter()
        for i in dict:
            for j in range(len(dict[0])):
                k = f"{i[:j]}*{i[j + 1:]}"
                d[k] += 1
                if d[k] == 2:
                    return True

        return False

# @lc code=end
