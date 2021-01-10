#
# @lc app=leetcode.cn id=1086 lang=python3
#
# [1086] 前五科的均分
#
# https://leetcode-cn.com/problems/high-five/description/
#
# algorithms
# Easy (70.78%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 5.8K
# Testcase Example:  '[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]'
#
# 给你一个不同学生的分数列表 items，其中 items[i] = [IDi, scorei] 表示 IDi 的学生的一科分数，你需要计算每个学生
# 最高的五科 成绩的 平均分。
# 
# 返回答案 result 以数对数组形式给出，其中 result[j] = [IDj, topFiveAveragej] 表示 IDj 的学生和他
# 最高的五科 成绩的 平均分。result 需要按 IDj  递增的 顺序排列 。
# 
# 学生 最高的五科 成绩的 平均分 的计算方法是将最高的五科分数相加，然后用 整数除法 除以 5 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：items =
# [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# 输出：[[1,87],[2,88]]
# 解释：
# ID = 1 的学生分数为 91、92、60、65、87 和 100 。前五科的平均分 (100 + 92 + 91 + 87 + 65) / 5 =
# 87
# ID = 2 的学生分数为 93、97、77、100 和 76 。前五科的平均分 (100 + 97 + 93 + 77 + 76) / 5 =
# 88.6，但是由于使用整数除法，结果转换为 88
# 
# 
# 示例 2：
# 
# 
# 输入：items =
# [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
# 输出：[[1,100],[7,100]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# items[i].length == 2
# 1 i 
# 0 i 
# 对于每个 IDi，至少 存在五个分数
# 
# 
#

# @lc code=start
import heapq
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = {}
        for i, score in items:
            if i not in d:
                d[i] = []
            heapq.heappush(d[i], score)
            if len(d[i]) > 5:
                heapq.heappop(d[i])

        return [[i, sum(d[i]) // 5] for i in sorted(d.keys())]

# @lc code=end
