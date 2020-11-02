#
# @lc app=leetcode.cn id=616 lang=python3
#
# [616] 给字符串添加加粗标签
#
# https://leetcode-cn.com/problems/add-bold-tag-in-string/description/
#
# algorithms
# Medium (44.93%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 4.4K
# Testcase Example:  '"abcxyz123"\n["abc","123"]'
#
# 给一个字符串 s 和一个字符串列表 dict ，你需要将在字符串列表中出现过的 s 的子串添加加粗闭合标签 <b> 和 </b>
# 。如果两个子串有重叠部分，你需要把它们一起用一个闭合标签包围起来。同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一个加粗标签包围。
# 
# 样例 1：
# 
# 输入：
# s = "abcxyz123"
# dict = ["abc","123"]
# 输出：
# "<b>abc</b>xyz<b>123</b>"
# 
# 
# 
# 
# 样例 2：
# 
# 输入：
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# 输出：
# "<b>aaabbc</b>c"
# 
# 
# 
# 
# 注意：
# 
# 
# 给定的 dict 中不会有重复的字符串，且字符串数目不会超过 100 。
# 输入中的所有字符串长度都在范围 [1, 1000] 内。
# 
# 
# 
# 
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        n = len(s)
        mask = [False] * n
        for i in range(n):
            p = s[i:]
            for w in dict:
                if p.startswith(w):
                    for j in range(i, min(i + len(w), n)):
                        mask[j] = True

        r = []
        for i, g in itertools.groupby(zip(s, mask), lambda z: z[1]):
            if i:
                r.append("<b>")
            r.append("".join(z[0] for z in g))
            if i:
                r.append("</b>")

        return "".join(r)

# @lc code=end
