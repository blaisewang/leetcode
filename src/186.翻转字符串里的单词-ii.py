#
# @lc app=leetcode.cn id=186 lang=python3
#
# [186] 翻转字符串里的单词 II
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (73.80%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 4.9K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
# 
# 示例：
# 
# 输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# 输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# 
# 注意：
# 
# 
# 单词的定义是不包含空格的一系列字符
# 输入字符串中不会包含前置或尾随的空格
# 单词与单词之间永远是以单个空格隔开的
# 
# 
# 进阶：使用 O(1) 额外空间复杂度的原地解法。
# 
#

# @lc code=start
from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = s[::-1]
        l = 0
        for i in range(len(st)):
            if st[i] == " ":
                st[l:i] = st[l:i][::-1]
                l = i + 1
                continue
            if i == len(st) - 1:
                st[l:i + 1] = st[l:i + 1][::-1]

        s[:] = st

# @lc code=end
