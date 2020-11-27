#
# @lc app=leetcode.cn id=737 lang=python3
#
# [737] 句子相似性 II
#
# https://leetcode-cn.com/problems/sentence-similarity-ii/description/
#
# algorithms
# Medium (44.67%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 5.1K
# Testcase Example:  '["great","acting","skills"]\n["fine","drama","talent"]\n[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]'
#
# 给定两个句子 words1, words2 （每个用字符串数组表示），和一个相似单词对的列表 pairs ，判断是否两个句子是相似的。
# 
# 例如，当相似单词对是 pairs = [["great", "fine"], ["acting","drama"],
# ["skills","talent"]]的时候，words1 = ["great", "acting", "skills"] 和 words2 =
# ["fine", "drama", "talent"] 是相似的。
# 
# 注意相似关系是 具有 传递性的。例如，如果 "great" 和 "fine" 是相似的，"fine" 和 "good" 是相似的，则 "great" 和
# "good" 是相似的。
# 
# 而且，相似关系是具有对称性的。例如，"great" 和 "fine" 是相似的相当于 "fine" 和 "great" 是相似的。
# 
# 并且，一个单词总是与其自身相似。例如，句子 words1 = ["great"], words2 = ["great"], pairs = []
# 是相似的，尽管没有输入特定的相似单词对。
# 
# 最后，句子只会在具有相同单词个数的前提下才会相似。所以一个句子 words1 = ["great"] 永远不可能和句子 words2 =
# ["doubleplus","good"] 相似。
# 
# 注：
# 
# 
# words1 and words2 的长度不会超过 1000。
# pairs 的长度不会超过 2000。
# 每个pairs[i] 的长度为 2。
# 每个 words[i] 和 pairs[i][j] 的长度范围为 [1, 20]。
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        g = defaultdict(list)
        for w1, w2 in pairs:
            g[w1].append(w2)
            g[w2].append(w1)

        for w1, w2 in zip(words1, words2):
            s, k = [w1], {w1}
            while s:
                word = s.pop()
                if word == w2:
                    break
                for nei in g[word]:
                    if nei not in k:
                        k.add(nei)
                        s.append(nei)
            else:
                return False

        return True

# @lc code=end
