#
# @lc app=leetcode.cn id=683 lang=python3
#
# [683] K 个关闭的灯泡
#
# https://leetcode-cn.com/problems/k-empty-slots/description/
#
# algorithms
# Hard (41.14%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 3.6K
# Testcase Example:  '[1,3,2]\n1'
#
# N 个灯泡排成一行，编号从 1 到 N 。最初，所有灯泡都关闭。每天只打开一个灯泡，直到 N 天后所有灯泡都打开。
# 
# 给你一个长度为 N 的灯泡数组 blubs ，其中 bulls[i] = x 意味着在第 (i+1) 天，我们会把在位置 x 的灯泡打开，其中 i 从 0
# 开始，x 从 1 开始。
# 
# 给你一个整数 K ，请你输出在第几天恰好有两个打开的灯泡，使得它们中间 正好 有 K 个灯泡且这些灯泡 全部是关闭的 。
# 
# 如果不存在这种情况，返回 -1 。如果有多天都出现这种情况，请返回 最小的天数 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# bulbs: [1,3,2]
# K: 1
# 输出：2
# 解释：
# 第一天 bulbs[0] = 1，打开第一个灯泡 [1,0,0]
# 第二天 bulbs[1] = 3，打开第三个灯泡 [1,0,1]
# 第三天 bulbs[2] = 2，打开第二个灯泡 [1,1,1]
# 返回2，因为在第二天，两个打开的灯泡之间恰好有一个关闭的灯泡。
# 
# 
# 示例 2：
# 
# 
# 输入：
# bulbs: [1,2,3]
# k: 1
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# bulbs 是一个由从 1 到 N 的数字构成的排列
# 0 
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        days = [0] * len(bulbs)
        for day, position in enumerate(bulbs, 1):
            days[position - 1] = day

        res = float("inf")
        left, right = 0, k + 1
        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i + k + 1
                    break
            else:
                res = min(res, max(days[left], days[right]))
                left, right = right, right + k + 1

        return res if res < float("inf") else -1

# @lc code=end
