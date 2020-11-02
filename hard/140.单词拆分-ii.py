#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (38.64%)
# Likes:    256
# Dislikes: 0
# Total Accepted:    22.9K
# Total Submissions: 59.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 
# 说明：
# 
# 
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# 
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        @lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]

            r = list()
            for i in range(index + 1, len(s) + 1):
                w = s[index:i]
                if w in words:
                    ns = backtrack(i)
                    for n in ns:
                        r.append(n.copy() + [w])

            return r

        return [" ".join(words[::-1]) for words in backtrack(0)]

# @lc code=end
