#
# @lc app=leetcode.cn id=1065 lang=python3
#
# [1065] 字符串的索引对
#
# https://leetcode-cn.com/problems/index-pairs-of-a-string/description/
#
# algorithms
# Easy (52.56%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 3.6K
# Testcase Example:  '"thestoryofleetcodeandme"\n["story","fleet","leetcode"]'
#
# 给出 字符串 text 和 字符串列表 words, 返回所有的索引对 [i, j] 使得在索引对范围内的子字符串
# text[i]...text[j]（包括 i 和 j）属于字符串列表 words。
# 
# 
# 
# 示例 1:
# 
# 输入: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# 输出: [[3,7],[9,13],[10,17]]
# 
# 
# 示例 2:
# 
# 输入: text = "ababa", words = ["aba","ab"]
# 输出: [[0,1],[0,2],[2,3],[2,4]]
# 解释: 
# 注意，返回的配对可以有交叉，比如，"aba" 既在 [0,2] 中也在 [2,4] 中
# 
# 
# 
# 
# 提示:
# 
# 
# 所有字符串都只包含小写字母。
# 保证 words 中的字符串无重复。
# 1 <= text.length <= 100
# 1 <= words.length <= 20
# 1 <= words[i].length <= 50
# 按序返回索引对 [i,j]（即，按照索引对的第一个索引进行排序，当第一个索引对相同时按照第二个索引对排序）。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        r = []

        for i in range(len(text)):
            for j in range(len(words)):
                if text[i:i + len(words[j])] == words[j]:
                    r.append([i, i + len(words[j]) - 1])

        return sorted(r, key=lambda e: (e[0], e[1]))

# @lc code=end
