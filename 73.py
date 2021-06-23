# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2020
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-06-29 10:41'
"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        zero_rows, zero_cols = set(), set()

        for row in range(0, m):
            for col in range(0, n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in range(0, m):
            for col in range(0, n):
                if row in zero_rows or col in zero_cols:
                    matrix[row][col] = 0


if __name__ == "__main__":
    matrix = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    Solution().setZeroes(matrix)
    print(matrix)