#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#
# https://leetcode-cn.com/problems/relative-ranks/description/
#
# algorithms
# Easy (52.24%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 12.9K
# Testcase Example:  '[5,4,3,2,1]'
#
# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold
# Medal", "Silver Medal", "Bronze Medal"）。
# 
# (注：分数越高的选手，排名越靠前。)
# 
# 示例 1:
# 
# 
# 输入: [5, 4, 3, 2, 1]
# 输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# 解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and
# "Bronze Medal").
# 余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
# 
# 提示:
# 
# 
# N 是一个正整数并且不会超过 10000。
# 所有运动员的成绩都不相同。
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        num_mapping = {num: index + 1 for index, num in enumerate(sorted(nums, reverse=True))}
        rank_mapping = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
        res = []
        for num in nums:
            rank = num_mapping[num]
            res.append(rank_mapping.get(rank, str(rank)))
        return res

# @lc code=end
