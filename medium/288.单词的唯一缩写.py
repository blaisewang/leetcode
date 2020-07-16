#
# @lc app=leetcode.cn id=288 lang=python3
#
# [288] 单词的唯一缩写
#
# https://leetcode-cn.com/problems/unique-word-abbreviation/description/
#
# algorithms
# Medium (32.70%)
# Likes:    3
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 4.6K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n' + '[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
#
# 一个单词的缩写需要遵循 <起始字母><中间字母数><结尾字母> 这样的格式。
# 
# 以下是一些单词缩写的范例：
# 
# a) it                      --> it    (没有缩写)
# 
# ⁠    1
# ⁠    ↓
# b) d|o|g                   --> d1g
# 
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# ⁠    ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n
# 
# ⁠             1
# ⁠    1---5----0
# ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# 
# 
# 假设你有一个字典和一个单词，请你判断该单词的缩写在这本字典中是否唯一。若单词的缩写在字典中没有任何 其他 单词与其缩写相同，则被称为单词的唯一缩写。
# 
# 示例：
# 
# 给定 dictionary = [ "deer", "door", "cake", "card" ]
# 
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.d = set(dictionary)
        self.c = Counter([self.to_abbr(w) for w in self.d])

    @staticmethod
    def to_abbr(w: str) -> str:
        return f"{w[0]}{len(w) - 2}{w[-1]}" if len(w) > 2 else w

    def isUnique(self, word: str) -> bool:
        return self.c[self.to_abbr(word)] == 0 or (self.c[self.to_abbr(word)] == 1 and word in self.d)

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
# @lc code=end
