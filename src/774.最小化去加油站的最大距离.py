#
# @lc app=leetcode.cn id=774 lang=python3
#
# [774] 最小化去加油站的最大距离
#
# https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station/description/
#
# algorithms
# Hard (58.46%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    736
# Total Submissions: 1.3K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10]\n9'
#
# 假设我们在一条水平数轴上，列表 stations 来表示各个加油站的位置，加油站分别在 stations[0], stations[1], ...,
# stations[N-1] 的位置上，其中 N = stations.length。
# 
# 现在我们希望增加 K 个新的加油站，使得相邻两个加油站的距离 D 尽可能的最小，请你返回 D 可能的最小值。
# 
# 示例：
# 
# 输入：stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# 输出：0.500000
# 
# 
# 注：
# 
# 
# stations.length 是在范围 [10, 2000] 内的整数
# stations[i] 是在范围 [0, 10^8] 内的整数
# K 是在范围 [1, 10^6] 内的整数
# 在 10^-6 以内的正确值会被视为正确的答案
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def possible(d: int):
            return sum(int((stations[i + 1] - stations[i]) / d) for i in range(len(stations) - 1)) <= K

        lo, hi = 0, 10 ** 8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi

        return lo

# @lc code=end
