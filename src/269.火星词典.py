#
# @lc app=leetcode.cn id=269 lang=python3
#
# [269] 火星词典
#
# https://leetcode-cn.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (33.41%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 11.8K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# 现有一种使用字母的全新语言，这门语言的字母顺序与英语顺序不同。
# 
# 假设，您并不知道其中字母之间的先后顺序。但是，会收到词典中获得一个 不为空的 单词列表。因为是从词典中获得的，所以该单词列表内的单词已经
# 按这门新语言的字母顺序进行了排序。
# 
# 您需要根据这个输入的列表，还原出此语言中已知的字母顺序。
# 
# 
# 
# 示例 1：
# 
# 输入:
# [
# ⁠ "wrt",
# ⁠ "wrf",
# ⁠ "er",
# ⁠ "ett",
# ⁠ "rftt"
# ]
# 输出: "wertf"
# 
# 
# 示例 2：
# 
# 输入:
# [
# ⁠ "z",
# ⁠ "x"
# ]
# 输出: "zx"
# 
# 
# 示例 3：
# 
# 输入:
# [
# ⁠ "z",
# ⁠ "x",
# ⁠ "z"
# ] 
# 输出: "" 
# 解释: 此顺序是非法的，因此返回 ""。
# 
# 
# 
# 
# 提示：
# 
# 
# 你可以默认输入的全部都是小写字母
# 若给定的顺序是不合法的，则返回空字符串即可
# 若存在多种可能的合法字母顺序，请返回其中任意一种顺序即可
# 
# 
#

# @lc code=start
from collections import deque, defaultdict
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = defaultdict(list)

        ind = {}
        for word in words:
            for w in word:
                ind[w] = 0

        for i in range(len(words) - 1):
            j = i + 1
            if len(words[i]) > len(words[j]) and words[j] == words[i][:len(words[j])]:
                return ""

            for k in range(min(len(words[i]), len(words[j]))):
                if words[i][k] == words[j][k]:
                    continue
                elif words[j][k] not in g[words[i][k]]:
                    g[words[i][k]].append(words[j][k])
                    ind[words[j][k]] += 1
                    break
                elif words[j][k] in g[words[i][k]]:
                    break

        q = deque([word for word in ind.keys() if ind[word] == 0])

        r = ""
        while q:
            word = q.popleft()
            r += word
            for w in g[word]:
                ind[w] -= 1
                if ind[w] == 0:
                    q.append(w)

        return r if len(r) == len(g) else ""

# @lc code=end
