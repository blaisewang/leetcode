#
# @lc app=leetcode.cn id=527 lang=python3
#
# [527] 单词缩写
#
# https://leetcode-cn.com/problems/word-abbreviation/description/
#
# algorithms
# Hard (56.33%)
# Likes:    27
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 2.7K
# Testcase Example:  '["like","god","internal","me","internet","interval","intension","face","intrusion"]'
#
# 给定一个由n个不重复非空字符串组成的数组，你需要按照以下规则为每个单词生成最小的缩写。
# 
# 
# 初始缩写由起始字母+省略字母的数量+结尾字母组成。
# 若存在冲突，亦即多于一个单词有同样的缩写，则使用更长的前缀代替首字母，直到从单词到缩写的映射唯一。换而言之，最终的缩写必须只能映射到一个单词。
# 若缩写并不比原单词更短，则保留原样。
# 
# 
# 示例:
# 
# 输入: ["like", "god", "internal", "me", "internet", "interval", "intension",
# "face", "intrusion"]
# 输出:
# ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# 
# 
# 
# 
# 注意:
# 
# 
# n和每个单词的长度均不超过 400。
# 每个单词的长度大于 1。
# 单词只由英文小写字母组成。
# 返回的答案需要和原数组保持同一顺序。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbrev(word: str, idx: int = 0) -> str:
            if len(word) - idx <= 3:
                return word
            return word[:idx + 1] + str(len(word) - idx - 2) + word[-1]

        res = [abbrev(word) for word in words]
        prefix = [0] * len(words)

        for i in range(len(words)):
            while True:
                dps = set()
                for j in range(i + 1, len(words)):
                    if res[i] == res[j]:
                        dps.add(j)

                if not dps:
                    break
                dps.add(i)
                for k in dps:
                    prefix[k] += 1
                    res[k] = abbrev(words[k], prefix[k])

        return res

# @lc code=end
