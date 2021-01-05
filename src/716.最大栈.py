#
# @lc app=leetcode.cn id=716 lang=python3
#
# [716] 最大栈
#
# https://leetcode-cn.com/problems/max-stack/description/
#
# algorithms
# Easy (45.78%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    2.4K
# Total Submissions: 5.4K
# Testcase Example:  '["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]\n[[],[5],[1],[5],[],[],[],[],[],[]]'
#
# 设计一个最大栈数据结构，既支持栈操作，又支持查找栈中最大元素。
# 
# 实现 MaxStack 类：
# 
# 
# MaxStack() 初始化栈对象
# void push(int x) 将元素 x 压入栈中。
# int pop() 移除栈顶元素并返回这个元素。
# int top() 返回栈顶元素，无需移除。
# int peekMax() 检索并返回栈中最大元素，无需移除。
# int popMax() 检索并返回栈中最大元素，并将其移除。如果有多个最大元素，只要移除 最靠近栈顶 的那个。
# 
# 
# 
# 
# 示例：
# 
# 
# 输入
# ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax",
# "pop", "top"]
# [[], [5], [1], [5], [], [], [], [], [], []]
# 输出
# [null, null, null, null, 5, 5, 1, 5, 1, 5]
# 
# 解释
# MaxStack stk = new MaxStack();
# stk.push(5);   // [5] - 5 既是栈顶元素，也是最大元素
# stk.push(1);   // [5, 1] - 栈顶元素是 1，最大元素是 5
# stk.push(5);   // [5, 1, 5] - 5 既是栈顶元素，也是最大元素
# stk.top();     // 返回 5，[5, 1, 5] - 栈没有改变
# stk.popMax();  // 返回 5，[5, 1] - 栈发生改变，栈顶元素不再是最大元素
# stk.top();     // 返回 1，[5, 1] - 栈没有改变
# stk.peekMax(); // 返回 5，[5, 1] - 栈没有改变
# stk.pop();     // 返回 1，[5] - 此操作后，5 既是栈顶元素，也是最大元素
# stk.top();     // 返回 5，[5] - 栈没有改变
# 
# 
# 
# 
# 提示：
# 
# 
# -10^7 
# 最多调用 104 次 push、pop、top、peekMax 和 popMax
# 调用 pop、top、peekMax 或 popMax 时，栈中 至少存在一个元素
# 
# 
# 
# 
# 进阶： 
# 
# 
# 试着设计解决方案：调用 top 方法的时间复杂度为 O(1) ，调用其他方法的时间复杂度为 O(logn) 。 
# 
# 
#


# @lc code=start
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_stack = []

    def push(self, x: int) -> None:
        m = max(x, self.max_stack[-1][1] if len(self.max_stack) else float("-inf"))
        self.max_stack.append((x, m))

    def pop(self) -> int:
        return self.max_stack.pop()[0]

    def top(self) -> int:
        return self.max_stack[-1][0]

    def peekMax(self) -> int:
        return self.max_stack[-1][1]

    def popMax(self) -> int:
        ts = []
        m = self.max_stack[-1][1]
        while self.max_stack[-1][0] != m:
            ts.append(self.max_stack.pop()[0])

        self.max_stack.pop()
        while ts:
            self.push(ts.pop())

        return m

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
# @lc code=end
