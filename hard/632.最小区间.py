#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#
# https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (38.58%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    13.7K
# Total Submissions: 23.3K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
# 
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。
# 
# 示例 1:
# 
# 
# 输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出: [20,24]
# 解释: 
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 
# 
# 注意:
# 
# 
# 给定的列表可能包含重复元素，所以在这里升序表示 >= 。
# 1 <= k <= 3500
# -10^5 <= 元素的值 <= 10^5
# 对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        n = len(nums)
        idxes = defaultdict(list)
        xi, xa = 10 ** 9, -10 ** 9
        for i, v in enumerate(nums):
            for x in v:
                idxes[x].append(i)
            xi = min(xi, *v)
            xa = max(xa, *v)

        f = [0] * n
        isd = 0
        l, r = xi, xi - 1
        bl, br = xi, xa

        while r < xa:
            r += 1
            if r in idxes:
                for x in idxes[r]:
                    f[x] += 1
                    if f[x] == 1:
                        isd += 1
                while isd == n:
                    if r - l < br - bl:
                        bl, br = l, r
                    if l in idxes:
                        for x in idxes[l]:
                            f[x] -= 1
                            if f[x] == 0:
                                isd -= 1
                    l += 1

        return [bl, br]

# @lc code=end
