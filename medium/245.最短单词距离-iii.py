#
# @lc app=leetcode.cn id=245 lang=python3
#
# [245] 最短单词距离 III
#
# https://leetcode-cn.com/problems/shortest-word-distance-iii/description/
#
# algorithms
# Medium (60.75%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 3.3K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"makes"\n"coding"'
#
# 给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。
# 
# word1 和 word2 是有可能相同的，并且它们将分别表示为列表中两个独立的单词。
# 
# 示例:
# 假设 words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# 输入: word1 = “makes”, word2 = “coding”
# 输出: 1
# 
# 
# 输入: word1 = "makes", word2 = "makes"
# 输出: 3
# 
# 
# 注意:
# 你可以假设 word1 和 word2 都在列表里。
# 
#

# @lc code=start
from typing import List


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = -1, -1
        d = float("inf")

        for i, w in enumerate(words):
            if w == word1:
                p1 = i
                if p2 != -1:
                    d = min(d, abs(p2 - p1))
            if w == word2:
                p2 = i
                if p1 != -1 and p1 != p2:
                    d = min(d, abs(p2 - p1))

        return d

# @lc code=end
