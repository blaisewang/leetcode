#
# @lc app=leetcode.cn id=444 lang=python3
#
# [444] 序列重建
#
# https://leetcode-cn.com/problems/sequence-reconstruction/description/
#
# algorithms
# Medium (21.93%)
# Likes:    17
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 6.3K
# Testcase Example:  '[1,2,3]\r\n[[1,2],[1,3]]\r'
#
# 验证原始的序列 org 是否可以从序列集 seqs 中唯一地重建。序列 org 是 1 到 n 整数的排列，其中 1 ≤ n ≤
# 10^4。重建是指在序列集 seqs 中构建最短的公共超序列。（即使得所有  seqs 中的序列都是该最短序列的子序列）。确定是否只可以从 seqs
# 重建唯一的序列，且该序列就是 org 。
# 
# 示例 1：
# 
# 输入：
# org: [1,2,3], seqs: [[1,2],[1,3]]
# 
# 输出：
# false
# 
# 解释：
# [1,2,3] 不是可以被重建的唯一的序列，因为 [1,3,2] 也是一个合法的序列。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：
# org: [1,2,3], seqs: [[1,2]]
# 
# 输出：
# false
# 
# 解释：
# 可以重建的序列只有 [1,2]。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
# 
# 输出：
# true
# 
# 解释：
# 序列 [1,2], [1,3] 和 [2,3] 可以被唯一地重建为原始的序列 [1,2,3]。
# 
# 
# 
# 
# 示例 4：
# 
# 输入：
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
# 
# 输出：
# true
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not org:
            return False
        if not seqs:
            return False

        seqs.sort()
        if not seqs[-1]:
            return False

        sns = set([])
        s_set = [set(seq) for seq in seqs]
        for s in s_set:
            sns |= s
        if set(org) != sns:
            return False

        adj = {i: [] for i in org}
        for seq in seqs:
            for i in range(len(seq) - 1):
                adj[seq[i]].append(seq[i + 1])

        ind = [0 for _ in range(len(adj))]

        for i in adj.values():
            for n in i:
                ind[n - 1] += 1

        s = []
        c = len(adj)
        q = [i + 1 for i in range(len(ind)) if ind[i] == 0]
        while q:
            if len(q) > 1:
                return False
            t = q.pop(0)
            s.append(t)
            ind[t - 1] = -1
            for i in adj[t]:
                ind[i - 1] -= 1
                if ind[i - 1] == 0:
                    q.append(i)
            c -= 1

        if c > 0:
            return False
        return s == org

# @lc code=end
