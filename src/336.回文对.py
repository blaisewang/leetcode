#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
# https://leetcode-cn.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (34.38%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 14.6K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
# 
# 示例 1:
# 
# 输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]] 
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 示例 2:
# 
# 输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]] 
# 解释: 可拼接成的回文串为 ["battab","tabbat"]
# 
#

# @lc code=start
from typing import List, Tuple


class Solution:
    def get_palindrome_parts(self, string: str) -> Tuple[list, list]:
        p, s = [], []
        for i in range(0, len(string) + 1):
            if string[:i] == string[:i][::-1]:
                p.append(string[i:][::-1])
            if string[i:] == string[i:][::-1]:
                s.append(string[:i][::-1])

        return p, s

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        r = []
        d = {w: i for i, w in enumerate(words)}
        for index, word in enumerate(words):
            p, s = self.get_palindrome_parts(word)
            for p in p:
                if p in d and index != d[p] and p[::-1] != word:
                    r.append([d[p], index])
            for s in s:
                if s in d and index != d[s]:
                    r.append([index, d[s]])
        return r

# @lc code=end
