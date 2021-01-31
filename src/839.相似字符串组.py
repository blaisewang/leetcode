#
# @lc app=leetcode.cn id=839 lang=python3
#
# [839] 相似字符串组
#
# https://leetcode-cn.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (36.18%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    4.5K
# Total Submissions: 11.2K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y
# 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。
# 
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，但是 "star" 不与
# "tars"，"rats"，或 "arts" 相似。
# 
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。注意，"tars" 和 "arts"
# 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 
# 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["tars","rats","arts","star"]
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["omv","ovm"]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# sum(strs[i].length) 
# strs[i] 只包含小写字母。
# strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
# 
# 
# 
# 
# 备注：
# 
# 字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。
# 
#

# @lc code=start
from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if not len(strs):
            return 0

        f = [i for i in range(len(strs))]

        def compare(a: str, b: str) -> bool:
            r = []
            for i in range(len(strs[0])):
                if a[i] != b[i]:
                    r.append(i)
                if len(r) > 2:
                    return False
            if len(r) == 1:
                return False
            if len(r) == 0:
                return True
            if a[r[0]] == b[r[1]] and a[r[1]] == b[r[0]]:
                return True
            return False

        def find(x: int) -> int:
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x: int, y: int):
            f[find(x)] = find(y)

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if compare(strs[i], strs[j]):
                    union(i, j)

        return sum(f[i] == i for i in range(len(strs)))

# @lc code=end
