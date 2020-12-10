#
# @lc app=leetcode.cn id=358 lang=python3
#
# [358] K 距离间隔重排字符串
#
# https://leetcode-cn.com/problems/rearrange-string-k-distance-apart/description/
#
# algorithms
# Hard (34.46%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 8.7K
# Testcase Example:  '"aabbcc"\n3'
#
# 给你一个非空的字符串 s 和一个整数 k，你要将这个字符串中的字母进行重新排列，使得重排后的字符串中相同字母的位置间隔距离至少为 k。
# 
# 所有输入的字符串都由小写字母组成，如果找不到距离至少为 k 的重排结果，请返回一个空字符串 ""。
# 
# 示例 1：
# 
# 输入: s = "aabbcc", k = 3
# 输出: "abcabc" 
# 解释: 相同的字母在新的字符串中间隔至少 3 个单位距离。
# 
# 
# 示例 2:
# 
# 输入: s = "aaabc", k = 3
# 输出: "" 
# 解释: 没有办法找到可能的重排结果。
# 
# 
# 示例 3:
# 
# 输入: s = "aaadbbcc", k = 2
# 输出: "abacabcd"
# 解释: 相同的字母在新的字符串中间隔至少 2 个单位距离。
# 
# 
#

# @lc code=start
from collections import Counter


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not s or k <= 1:
            return s

        counter = Counter(s)
        a = list(map(list, counter.most_common()))
        c, t = a[0]

        if k * (t - 1) + sum([1 for c1, t1 in a if t1 == t]) > len(s):
            return ""

        tmp = [[] for _ in range(t)]
        for i in range(t):
            for j, (c1, t1) in enumerate(a):
                if t1 == 0:
                    continue
                tmp[i].append(c1)
                a[j][1] -= 1
                if len(tmp[i]) == k:
                    break

        for i in range(t):
            for j, (c1, t1) in enumerate(a):
                if t1 == 0:
                    continue
                tmp[i].append(c1)
                a[j][1] -= 1

        r = ""
        for w in tmp:
            r += "".join(w)

        return r

# @lc code=end
