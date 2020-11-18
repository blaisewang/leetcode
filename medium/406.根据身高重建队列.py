#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
# https://leetcode-cn.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (67.71%)
# Likes:    541
# Dislikes: 0
# Total Accepted:    47.7K
# Total Submissions: 70.3K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。
# 编写一个算法来重建这个队列。
# 
# 注意：
# 总人数少于1100人。
# 
# 示例
# 
# 
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        r = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            r[p[1]:p[1]] = [p]

        return r

# @lc code=end
