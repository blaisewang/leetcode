#
# @lc app=leetcode.cn id=1258 lang=python3
#
# [1258] 近义词句子
#
# https://leetcode-cn.com/problems/synonymous-sentences/description/
#
# algorithms
# Medium (57.36%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    936
# Total Submissions: 1.6K
# Testcase Example:  '[["happy","joy"],["sad","sorrow"],["joy","cheerful"]]\n"I am happy today but was sad yesterday"
#
# 给你一个近义词表 synonyms 和一个句子 text ， synonyms 表中是一些近义词对 ，你可以将句子 text
# 中每个单词用它的近义词来替换。
# 
# 请你找出所有用近义词替换后的句子，按 字典序排序 后返回。
# 
# 
#  
# 示例 1：
# 
# 
# 输入：
# synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
# text = "I am happy today but was sad yesterday"
# 输出：
# ["I am cheerful today but was sad yesterday",
# "I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= synonyms.length <= 10
# synonyms[i].length == 2
# synonyms[0] != synonyms[1]
# 所有单词仅包含英文字母，且长度最多为 10 。
# text 最多包含 10 个单词，且单词间用单个空格分隔开。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        d, s = {}, text.split()
        for i, j in synonyms:
            d[i], d[j] = d.get(i, [i]), d.get(j, [j])
            if d[i] is not d[j]:
                d[i].extend(d[j])
                for k in d[j]:
                    d[k] = d[i]

        r = []

        def f(index: int, t: list):
            if index == len(s):
                r.append(" ".join(t))
            else:
                [*map(lambda x: f(index + 1, t + [x]), d[s[index]] if s[index] in d else [s[index]])]

        f(0, [])
        return sorted(r)

# @lc code=end
