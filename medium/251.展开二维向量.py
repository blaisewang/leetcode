#
# @lc app=leetcode.cn id=251 lang=python3
#
# [251] 展开二维向量
#
# https://leetcode-cn.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (53.90%)
# Likes:    20
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 2.7K
# Testcase Example:  '["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]\n' + '[[[[1,2],[3],[4]]],[null],[null],[null],[null],[null],[null],[null]]'
#
# 请设计并实现一个能够展开二维向量的迭代器。该迭代器需要支持 next 和 hasNext 两种操作。、
# 
# 示例：
# 
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
# 
# iterator.next(); // 返回 1
# iterator.next(); // 返回 2
# iterator.next(); // 返回 3
# iterator.hasNext(); // 返回 true
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 4
# iterator.hasNext(); // 返回 false
# 
# 
# 
# 
# 注意：
# 
# 
# 请记得 重置 在 Vector2D 中声明的类变量（静态变量），因为类变量会 在多个测试用例中保持不变，影响判题准确。请 查阅 这里。
# 你可以假定 next() 的调用总是合法的，即当 next() 被调用时，二维向量总是存在至少一个后续元素。
# 
# 
# 
# 
# 进阶：
# 
# 尝试在代码中仅使用 C++ 提供的迭代器 或 Java 提供的迭代器。
# 
#

# @lc code=start
from typing import List


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.i = 0
        self.o = 0

    def advance_to_next(self):
        while self.o < len(self.v) and self.i == len(self.v[self.o]):
            self.o += 1
            self.i = 0

    def next(self) -> int:
        self.advance_to_next()
        r = self.v[self.o][self.i]
        self.i += 1
        return r

    def hasNext(self) -> bool:
        self.advance_to_next()
        return self.o < len(self.v)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
