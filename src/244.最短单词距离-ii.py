#
# @lc app=leetcode.cn id=244 lang=python3
#
# [244] 最短单词距离 II
#
# https://leetcode-cn.com/problems/shortest-word-distance-ii/description/
#
# algorithms
# Medium (50.94%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 4.2K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n' + '[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]'
#
# 请设计一个类，使该类的构造函数能够接收一个单词列表。然后再实现一个方法，该方法能够分别接收两个单词 word1 和
# word2，并返回列表中这两个单词之间的最短距离。您的方法将被以不同的参数调用 多次。
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
# 注意:
# 你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
# 
#

# @lc code=start
from typing import List


class WordDistance:

    def __init__(self, words: List[str]):
        self.d = {}
        for i, w in enumerate(words):
            self.d.setdefault(w, []).append(i)

    def shortest(self, word1: str, word2: str) -> int:
        p1, p2 = 0, 0
        md = float("inf")
        l1, l2 = self.d[word1], self.d[word2]

        while p1 < len(l1) and p2 < len(l2):
            md = min(md, abs(l1[p1] - l2[p2]))
            if l1[p1] < l2[p2]:
                p1 += 1
            else:
                p2 += 1
        return md

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
# @lc code=end
