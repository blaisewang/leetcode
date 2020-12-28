#
# @lc app=leetcode.cn id=243 lang=python3
#
# [243] 最短单词距离
#
# https://leetcode-cn.com/problems/shortest-word-distance/description/
#
# algorithms
# Easy (65.45%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 8.6K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"coding"\n"practice"'
#
# 给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。
# 
# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"]
# 
# 输入: word1 = “coding”, word2 = “practice”
# 输出: 3
# 
# 
# 输入: word1 = "makes", word2 = "coding"
# 输出: 1
# 
# 
# 注意:
# 你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
# 
#

# @lc code=start
from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        s = len(words)
        i = -1
        for w in words:
            i += 1
            if w == word1:
                j = -1
                for b in words:
                    j += 1
                    if b == word2 and s > abs(i - j):
                        s = abs(i - j)

        return s

# @lc code=end
