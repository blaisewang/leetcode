#
# @lc app=leetcode.cn id=281 lang=python3
#
# [281] 锯齿迭代器
#
# https://leetcode-cn.com/problems/zigzag-iterator/description/
#
# algorithms
# Medium (74.39%)
# Likes:    16
# Dislikes: 0
# Total Accepted:    1.1K
# Total Submissions: 1.5K
# Testcase Example:  '[1,2]\n[3,4,5,6]'
#
# 给出两个一维的向量，请你实现一个迭代器，交替返回它们中间的元素。
# 
# 示例:
# 
# 输入:
# v1 = [1,2]
# v2 = [3,4,5,6] 
# 
# 输出: [1,3,2,4,5,6]
# 
# 解析: 通过连续调用 next 函数直到 hasNext 函数返回 false，
# next 函数返回值的次序应依次为: [1,3,2,4,5,6]。
# 
# 拓展：假如给你 k 个一维向量呢？你的代码在这种情况下的扩展性又会如何呢?
# 
# 拓展声明：
# “锯齿” 顺序对于 k > 2 的情况定义可能会有些歧义。所以，假如你觉得 “锯齿” 这个表述不妥，也可以认为这是一种 “循环”。例如：
# 
# 输入:
# [1,2,3]
# [4,5,6,7]
# [8,9]
# 
# 输出: [1,4,8,2,5,9,3,6,7].
# 
# 
#

# @lc code=start
from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.c = 0
        self.l = 2
        self.idx = [0, 0]
        self.nums = [v1, v2]

    def next(self) -> int:
        n = self.c
        while self.idx[n] == len(self.nums[n]):
            n = (n + 1) % self.l
        res = self.nums[n][self.idx[n]]
        self.idx[n] += 1
        self.c = (n + 1) % self.l
        return res

    def hasNext(self) -> bool:
        for i in range(len(self.idx)):
            if self.idx[i] != len(self.nums[i]):
                return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
