#
# @lc app=leetcode.cn id=1257 lang=python3
#
# [1257] 最小公共区域
#
# https://leetcode-cn.com/problems/smallest-common-region/description/
#
# algorithms
# Medium (53.86%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 2.5K
# Testcase Example:  '[["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]]\n"Quebec"\n"New York"
#
# 给你一些区域列表 regions ，每个列表的第一个区域都包含这个列表内所有其他区域。
# 
# 很自然地，如果区域 X 包含区域 Y ，那么区域 X  比区域 Y 大。
# 
# 给定两个区域 region1 和 region2 ，找到同时包含这两个区域的 最小 区域。
# 
# 如果区域列表中 r1 包含 r2 和 r3 ，那么数据保证 r2 不会包含 r3 。
# 
# 数据同样保证最小公共区域一定存在。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# 输出："North America"
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= regions.length <= 10^4
# region1 != region2
# 所有字符串只包含英文字母和空格，且最多只有 20 个字母。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        s, d = set(), {i: j for j, *r in regions for i in r}
        while region1 in d:
            s.add(region1)
            region1 = d[region1]

        while region2 in d:
            if region2 in s:
                return region2
            region2 = d[region2]

        return region2

# @lc code=end
