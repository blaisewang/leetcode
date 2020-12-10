#
# @lc app=leetcode.cn id=465 lang=python3
#
# [465] 最优账单平衡
#
# https://leetcode-cn.com/problems/optimal-account-balancing/description/
#
# algorithms
# Hard (51.36%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 2.2K
# Testcase Example:  '[[0,1,10],[2,0,5]]'
#
# 一群朋友在度假期间会相互借钱。比如说，小爱同学支付了小新同学的午餐共计 10 美元。如果小明同学支付了小爱同学的出租车钱共计 5
# 美元。我们可以用一个三元组 (x, y, z) 表示一次交易，表示 x 借给 y 共计 z 美元。用 0, 1, 2
# 表示小爱同学、小新同学和小明同学（0, 1, 2 为人的标号），上述交易可以表示为 [[0, 1, 10], [2, 0, 5]]。
# 
# 给定一群人之间的交易信息列表，计算能够还清所有债务的最小次数。
# 
# 注意：
# 
# 
# 一次交易会以三元组 (x, y, z) 表示，并有 x ≠ y 且 z > 0。
# 人的标号可能不是按顺序的，例如标号可能为 0, 1, 2 也可能为 0, 2, 6。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：
# [[0,1,10], [2,0,5]]
# 
# 输出：
# 2
# 
# 解释：
# 人 #0 给人 #1 共计 10 美元。
# 人 #2 给人 #0 共计 5 美元。
# 
# 需要两次交易。一种方式是人 #1 分别给人 #0 和人 #2 各 5 美元。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：
# [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# 
# 输出：
# 1
# 
# 解释：
# 人 #0 给人 #1 共计 10 美元。Person #0 gave person #1 $10.
# 人 #1 给人 #0 共计 1 美元。Person #1 gave person #0 $1.
# 人 #1 给人 #2 共计 5 美元。Person #1 gave person #2 $5.
# 人 #2 给人 #0 共计 5 美元。Person #2 gave person #0 $5.
# 
# 因此，人 #1 需要给人 #0 共计 4 美元，所有的债务即可还清。
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        person = defaultdict(int)
        for x, y, z in transactions:
            person[x] -= z
            person[y] += z

        r = float("inf")
        ac = list(person.values())

        def dfs(i: int, c: int):
            nonlocal r
            if c >= r:
                return
            while i < len(ac) and ac[i] == 0:
                i += 1

            if i == len(ac):
                r = min(r, c)
                return

            for j in range(i + 1, len(ac)):
                if ac[i] * ac[j] < 0:
                    ac[j] += ac[i]
                    dfs(i + 1, c + 1)
                    ac[j] -= ac[i]

        dfs(0, 0)

        return r

# @lc code=end
