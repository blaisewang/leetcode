#
# @lc app=leetcode.cn id=631 lang=python3
#
# [631] 设计 Excel 求和公式
#
# https://leetcode-cn.com/problems/design-excel-sum-formula/description/
#
# algorithms
# Hard (26.26%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    829
# Total Submissions: 3.2K
# Testcase Example:  '["Excel","get","set","get"]\n[[3,"C"],[1,"A"],[1,"A",1],[1,"A"]]'
#
# 你的任务是实现 Excel 的求和功能，具体的操作如下：
# 
# Excel(int H, char W): 这是一个构造函数，输入表明了 Excel 的高度和宽度。H 是一个正整数，范围从 1 到 26，代表高度。W
# 是一个字符，范围从 'A' 到 'Z'，宽度等于从 'A' 到 W 的字母个数。Excel 表格是一个高度 * 宽度的二维整数数组，数组中元素初始化为
# 0。第一行下标从 1 开始，第一列下标从 'A' 开始。
# 
# 
# 
# void Set(int row, char column, int val): 设置 C(row, column) 中的值为 val。
# 
# 
# 
# int Get(int row, char column): 返回 C(row, column) 中的值。
# 
# 
# 
# int Sum(int row, char column, List of Strings : numbers): 这个函数会将计算的结果放入
# C(row, column) 中，计算的结果等于在 numbers
# 中代表的所有元素之和，这个函数同时也会将这个结果返回。求和公式会一直计算更新结果直到这个公式被其他的值或者公式覆盖。
# 
# numbers 是若干字符串的集合，每个字符串代表单个位置或一个区间。如果这个字符串表示单个位置，它的格式如下：ColRow，例如 "F7" 表示位置
# (7, F) 。如果这个字符串表示一个区间，它的格式如下：ColRow1:ColRow2。区间就是左上角为 ColRow1 右下角为 ColRow2
# 的长方形。
# 
# 
# 
# 样例 1 ：
# 
# 
# 
# Excel(3,"C"); 
# // 构造一个 3*3 的二维数组，初始化全是 0。
# //   A B C
# // 1 0 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Set(1, "A", 2);
# // 设置 C(1,"A") 为 2。
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 0
# 
# Sum(3, "C", ["A1", "A1:B2"]);
# // 将 C(3,"C") 的值设为 C(1,"A") 单点，左上角为 C(1,"A") 右下角为 C(2,"B") 的长方形，所有元素之和。返回值
# 4。 
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 4
# 
# Set(2, "B", 2);
# // 将 C(2,"B") 设为 2。 注意 C(3, "C") 的值也同时改变。
# //   A B C
# // 1 2 0 0
# // 2 0 2 0
# // 3 0 0 6
# 
# 
# 
# 
# 注释 ：
# 
# 
# 你可以认为不会出现循环求和的定义，比如说： A1 = sum(B1) ，B1 = sum(A1)。
# 测试数据中，字母表示用双引号。
# 请记住清零 Excel 类中的变量，因为静态变量、类变量会在多组测试数据中保存之前结果。详情请看这里。
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
from typing import Tuple, List


class Cell:
    def __repr__(self):
        res = "".join(f"(({k[0]},{k[1]}):{v})" for k, v in self.edges.items())
        return str(self.val) + res

    def __init__(self, val):
        self.val = val
        self.edges = Counter()


class Excel:

    def __init__(self, H: int, W: str):
        self.m = [[Cell(0) for _ in range(ord(W) - ord("A") + 1)] for _ in range(H)]

    def dfs(self, i: int, j: int) -> int:
        cell = self.m[i][j]
        if len(cell.edges) == 0:
            return cell.val

        return sum(self.dfs(*k) * v for k, v in cell.edges.items())

    @staticmethod
    def get_index(r: int, c: str) -> Tuple[int, int]:
        return r - 1, ord(c) - ord("A")

    @staticmethod
    def str_2_index(s: str) -> Tuple[int, int]:
        return int(s[1:]) - 1, ord(s[0]) - ord("A")

    def set(self, r: int, c: str, v: int):
        i, j = self.get_index(r, c)
        self.m[i][j].val = v
        self.m[i][j].edges = Counter()

    def get(self, r: int, c: str) -> int:
        i, j = self.get_index(r, c)
        return self.dfs(i, j)

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        i, j = self.get_index(r, c)
        cell = self.m[i][j]
        cell.val = 0
        cell.edges = Counter()

        for string in strs:
            if ":" not in string:
                ni, nj = self.str_2_index(string)
                cell.edges[(ni, nj)] += 1
            else:
                start, end = string.split(":")
                i_start, j_start = self.str_2_index(start)
                i_end, j_end = self.str_2_index(end)
                for ni in range(i_start, i_end + 1):
                    for nj in range(j_start, j_end + 1):
                        cell.edges[(ni, nj)] += 1

        return self.dfs(i, j)

# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)
# @lc code=end
