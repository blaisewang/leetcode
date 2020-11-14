#
# @lc app=leetcode.cn id=1151 lang=python3
#
# [1151] 最少交换次数来组合所有的 1
#
# https://leetcode-cn.com/problems/minimum-swaps-to-group-all-1s-together/description/
#
# algorithms
# Medium (47.05%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 5.5K
# Testcase Example:  '[1,0,1,0,1]'
#
# 给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,0,1,0,1]
# 输出：1
# 解释： 
# 有三种可能的方法可以把所有的 1 组合在一起：
# [1,1,1,0,0]，交换 1 次；
# [0,1,1,1,0]，交换 2 次；
# [0,0,1,1,1]，交换 1 次。
# 所以最少的交换次数为 1。
# 
# 
# 示例 2：
# 
# 输入：[0,0,0,1,0]
# 输出：0
# 解释： 
# 由于数组中只有一个 1，所以不需要交换。
# 
# 
# 示例 3：
# 
# 输入：[1,0,1,0,1,0,0,1,1,0,1]
# 输出：3
# 解释：
# 交换 3 次，一种可行的只用 3 次交换的解决方案是 [0,0,0,0,0,1,1,1,1,1,1]。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= data.length <= 10^5
# 0 <= data[i] <= 1
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        zc, oc, s = 0, 0, sum(data)

        j, r = 0, 0
        for i in range(len(data)):
            if data[i] == 0:
                zc += 1
            else:
                oc += 1

            while zc > s - oc:
                if data[j] == 0:
                    zc -= 1
                else:
                    oc -= 1
                j += 1
            r = max(r, oc)

        return s - r

# @lc code=end
